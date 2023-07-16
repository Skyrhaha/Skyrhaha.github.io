## 概述
### 参考文档
- `.NET`官方文档 https://docs.microsoft.com/en-us/dotnet/
- `C#`官方文档 https://docs.microsoft.com/en-us/dotnet/csharp/
- visual studio下载 https://visualstudio.microsoft.com/zh-hans/downloads/
- (`vscode+.net`)sdk下载地址 https://dotnet.microsoft.com/en-us/download

### .NET标准与实现
- `.NET`当前一种标准,多种实现
- 标准为: `.NET Standard`
- 实现为: `.NET Core`, `.NET Framework`, `Mono`, `UWP`

> .NET Core
- 完全实现`.NET Standard`、开源跨平台、可以在Windows、Linux、macOS平台运行


> .NET Framework
1. 4.5以上实现`.NET Standard`
2. 部分开源、仅支持Windows平台、有很多独有的框架如WPF
3. 成熟度高

> Mono
- 用于Android和所有Apple系统,如Xamarin和Unity,适合于非微软的移动设备

> UWP(通用windows平台)
- 统一微软各类设备Windows,Xbox,Windows phone等

### .NET应用场景
- 桌面应用(winform、wpf等)
- web应用(`asp.net`)
- Unity 3D(游戏开发 or 虚拟现实)

### .NET编程语言
`C#`,`VB`,`F#`

### 开发环境
> visual studio
1. 官网下载installer.exe
2. 通过installer安装（选择需要安装的包,如果没选后续可以再次通过installer更改来添加）
3. 启动: win+r => devenv可以启动vs或者双击vs图标启动
4. vs常用操作:
   - 检查语法错误: 生成->解决方案(F6)
   - 设置字体和颜色: 工具->选项 
   - 设置启动项目: 解决方案（右键) -> 属性 -> 当前选定内容
   - 项目卸载/加载

> visual studio code + sdk
1. vscode安装
1. vscode对应C#插件安装
   - C#
1. vscode常用操作:
   - code -r *xxxdir*(如../TodoApi) 使用vscode打开对应目录

> Rider (JetBrains)


## C#基础

### 项目文件结构介绍
1. 解决方案、项目、类之间的关系
1. 目录结构
    - 解决方案目录
    - .suo文件
    - .sln文件：解决方案文件
    - 项目目录
      - .csproj文件：项目文件
      - Program.cs 组成部分
      - 引用命名空间

## webapi示例

### 参考文档
- [Create a web API with ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-6.0&tabs=visual-studio-code)

### Prerequisites
1. Visual Studio Code
1. C# for Visual Studio Code
1. .NET 6.x SDK

### Create a web project
1. Open the integrated terminal
1. Change directories(cd) to the folder that will contain the project folder
1. Run the following commands:
   - `dotnet new webapi -o teacup.net --no-https`
   - `code -r ./teacup.net`
1. Run the app
   - `dotnet run`
   - In a browser, navigate to `http://localhost:<port>`/swagger,where `<port>` is the randomly chosen number displayed in the output
   - Navigate to `https://localhost:<port>/weatherforecast` url
1. dotnet --version #查看版本: 6.0.200

### Add a model class
1. Add a folder named Models
1. Add a TodoItem.cs class to the Models  folder with the following code:
   ```csharp
   namespace Teacup.Models
   {
      public class TodoItem
      {
         public long Id { get; set; }
         public string? Name { get; set; }
         public bool IsComplete { get; set; }
      }
   }
   ```

### Add a database context
1. `dotnet add package Microsoft.EntityFrameworkCore.InMemory`
1. Add a TodoContext.cs file to the Models folder:
   ```csharp
   using Microsoft.EntityFrameworkCore;

   namespace Teacup.Models
   {
      public class TodoContext : DbContext
      {
         public DbSet<TodoItem> TodoItems { get; set; } = null!;

         public TodoContext(DbContextOptions<TodoContext> options) : base(options)
         {
               
         }
      }
   }
   ```
### Register the database context
1. Update Program.cs
   ```csharp
   ...
   using Microsoft.EntityFrameworkCore;
   using Teacup.Models;

   ...

   builder.Services.AddDbContext<TodoContext>(opt =>
      opt.UseInMemoryDatabase("TodoList"));
    ```

### Scaffold a controller
```bash
# 代码生成器引用
dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design

dotnet add package Microsoft.EntityFrameworkCore.Design

# SqlServer的Entity FrameworkCore的驱动程序
dotnet add package Microsoft.EntityFrameworkCore.SqlServer

# 安装代码生成器
dotnet tool install -g dotnet-aspnet-codegenerator

#使用代码生成器生成TodoItemsController.cs
dotnet aspnet-codegenerator controller -name TodoItemsController -async -api -m TodoItem -dc TodoContext -outDir Controllers
```

> TodoItemsController.cs
```csharp
#nullable disable
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Teacup.Models;

namespace teacup.net.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TodoItemsController : ControllerBase
    {
        private readonly TodoContext _context;

        public TodoItemsController(TodoContext context)
        {
            _context = context;
        }

        // GET: api/TodoItems
        [HttpGet]
        public async Task<ActionResult<IEnumerable<TodoItem>>> GetTodoItems()
        {
            return await _context.TodoItems.ToListAsync();
        }

        // GET: api/TodoItems/5
        [HttpGet("{id}")]
        public async Task<ActionResult<TodoItem>> GetTodoItem(long id)
        {
            var todoItem = await _context.TodoItems.FindAsync(id);

            if (todoItem == null)
            {
                return NotFound();
            }

            return todoItem;
        }

        // PUT: api/TodoItems/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutTodoItem(long id, TodoItem todoItem)
        {
            if (id != todoItem.Id)
            {
                return BadRequest();
            }

            _context.Entry(todoItem).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!TodoItemExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/TodoItems
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<TodoItem>> PostTodoItem(TodoItem todoItem)
        {
            _context.TodoItems.Add(todoItem);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetTodoItem", new { id = todoItem.Id }, todoItem);
        }

        // DELETE: api/TodoItems/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTodoItem(long id)
        {
            var todoItem = await _context.TodoItems.FindAsync(id);
            if (todoItem == null)
            {
                return NotFound();
            }

            _context.TodoItems.Remove(todoItem);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool TodoItemExists(long id)
        {
            return _context.TodoItems.Any(e => e.Id == id);
        }
    }
}
```

## web常用技术实现
1. 如何进行系统搭建
1. 如何提供RESTful API
   - 接口定义
   - 接口路由
   - 请求响应绑定
   - 数据序列化
1. 数据库如何访问
   - 数据库基本操作
   - 数据库事务
1. 系统安全验证如何设置
1. 缓存如何访问
1. 如何设置异常处理
1. 如何记录跟踪日志
1. 如何自动管理接口文档
1. 如何设置定时任务
1. 如何http调用其他系统

