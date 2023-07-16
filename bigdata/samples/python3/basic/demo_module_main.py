import demo_module as dm

print(f"dir(demo_module)={dir(dm)}")
print(f"{dm._privateVar}")
print(f"{dm.__golbalVar}")
dm.hello()

