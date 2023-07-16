var defaultOptions = {
    headings: 'h1, h2',
    scope: '.markdown-section',

    // To make work
    title: 'Contents',
    listType: 'ul',
}

// Element builders
var tocHeading = function (Title) {
    return document.createElement('h2').appendChild(
        document.createTextNode(Title)
    )
}

var aTag = function (src) {
    var a = document.createElement('a');
    var content = src.firstChild.innerHTML;

    // Use this to clip text w/ HTML in it.
    // https://github.com/arendjr/text-clipper
    a.innerHTML = content;
    a.href = src.firstChild.href;
    a.onclick = tocClick

    // In order to remove this gotta fix the styles.
    a.setAttribute('class', 'anchor');

    return a
};

var tocClick = function (e) {
    // var divs = document.querySelectorAll('.page_toc .active');

    // console.log(`tocClick:divs=${divs}`);

    // // Remove the previous classes
    // [].forEach.call(divs, function (div) {

    //     console.log(`div=${div}`);
    //     div.setAttribute('class', 'anchor')
    // });

    // Make sure this is attached to the parent not itself
    // console.log(e)
    e.currentTarget.setAttribute('class', 'active')
};

//------------------------------------------------------------------------

var getHeaders = function (selector) {
    var headings2 = document.querySelectorAll(selector);
    var ret = [];

    [].forEach.call(headings2, function (heading) {
        ret = ret.concat(heading);
    });

    return ret;
};

var getLevel = function (header) {
    var decs = header.match(/\d/g);

    return decs ? Math.min.apply(null, decs) : 1;
};

const buildToc = function (headers) {
    preLevel = -1

    html = ''

    function get_a(h) {
        return `<a href='${h.firstChild.href}'  class='anchor'>${h.firstChild.innerHTML}</a>`
    }

    back = Array.of()
    for (var h of headers) {

        // console.log(h)

        id = h.id
        level = parseInt(h.localName.charAt(1))

        if (preLevel == -1) {
            html += '<ol>'
            back.push('</ol>')

            html += '<li>'
            html += get_a(h)
            back.push('</li>')
        } else if (level > preLevel) {
            html += '<ol>'
            back.push('</ol>')

            html += '<li>'
            html += get_a(h)
            back.push('</li>')

        } else if (level == preLevel) {

            html += back.pop()

            html += '<li>'
            html += get_a(h)
            back.push('</li>')
        } else {
            // h3 -> h1 => 
            offset = preLevel - level
            while (offset > 0) {
                html += back.pop()
                html += back.pop()
                offset--
            }
            html += '<li>'
            html += get_a(h)
            back.push('</li>')
        }

        // console.log('html =====', html)

        preLevel = level
    }

    return html

};

// Docsify plugin functions
function tocPlugin(hook, vm) {
    var userOptions = vm.config.toc;

    hook.mounted(function () {
        console.log('toc hook mounted.')
        var content = window.Docsify.dom.find(".content");
        if (content) {
            var nav = window.Docsify.dom.create("aside", "");
            window.Docsify.dom.toggleClass(nav, "add", "nav");
            window.Docsify.dom.before(content, nav);
        }
    });

    hook.beforeEach(function (markdown) {
        // ...
        console.log('toc beforeEach...')
        return markdown;
    });

    hook.afterEach(function (html) {
        // ...
        console.log('toc afterEach...')

        const parser = new DOMParser();

        const doc = parser.parseFromString(html, "text/html");
        var headers = doc.querySelectorAll('h1,h2,h3,h4,h5,h6')

        var ret = [];
        [].forEach.call(headers, function (h) {
            ret = ret.concat(h);
        });

        headers = ret.filter(h => h.id)
        const headersHTML = buildToc(headers)

        window.$docsify['toc_content'] = headersHTML
        return html;
    });

    hook.ready(function () {
        // ...
        console.log('toc ready...')
    });

    hook.doneEach(function () {
        console.log('toc hook doneEach start...')

        var nav = document.querySelectorAll('.nav')[0]
        var t = Array.from(document.querySelectorAll('.nav'))

        if (!nav) {
            return;
        }

        // Just unset it for now.
        if (!window.$docsify['toc_content']) {
            nav.innerHTML = null
            return;
        }

        var container = document.createElement('div');
        container.setAttribute('class', 'page_toc');

        container.innerHTML = `
                <p class='title'>${userOptions.title}</p>
                ${window.$docsify['toc_content']}
        `
        // Existing TOC
        var tocChild = document.querySelectorAll('.nav .page_toc');

        if (tocChild.length > 0) {
            tocChild[0].parentNode.removeChild(tocChild[0]);
        }

        nav.appendChild(container);

        console.log('toc hook doneEach end')
    });
}

// Docsify plugin options
window.$docsify['toc'] = Object.assign(defaultOptions, window.$docsify['toc']);
window.$docsify.plugins = [].concat(tocPlugin, window.$docsify.plugins);