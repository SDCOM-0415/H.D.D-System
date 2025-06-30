# 构建指南

本项目使用GitHub Actions自动构建Windows和macOS平台的可执行程序。

## GitHub Actions自动构建

项目已配置GitHub Actions工作流，可以自动构建Windows的.exe程序和macOS的.app/.dmg程序。

### 触发构建

构建会在以下情况自动触发：
- 向`main`或`master`分支推送代码
- 创建针对`main`或`master`分支的Pull Request
- 手动触发工作流（在GitHub仓库的Actions标签页中）

### 获取构建结果

1. 在GitHub仓库页面，点击"Actions"标签
2. 选择最新的成功构建
3. 在构建详情页面底部的"Artifacts"部分，可以下载以下文件：
   - `HDD-System-Windows`：Windows可执行程序
   - `HDD-System-macOS-app`：macOS应用程序(.app)
   - `HDD-System-macOS-dmg`：macOS磁盘镜像(.dmg)

## 手动构建指南

如果你想在本地构建应用程序，可以按照以下步骤操作：

### Windows构建

1. 安装依赖：
   ```
   pip install -r requirements.windows.txt
   pip install pyinstaller
   ```

2. 使用PyInstaller构建：
   ```
   pyinstaller --name="HDD-System" --windowed --icon=Icon.ico --add-data="*.png;." --add-data="*.mp3;." --add-data="*.wav;." --add-data="*.ttf;." --add-data="Icon.ico;." Main.PY
   ```

3. 构建结果将位于`dist/HDD-System/`目录

### macOS构建

1. 安装依赖：
   ```
   pip install -r requirements.macos.txt
   pip install pyinstaller
   ```

2. 使用PyInstaller构建：
   ```
   pyinstaller --name="HDD-System" --windowed --icon=Icon.ico --add-data="*.png:." --add-data="*.mp3:." --add-data="*.wav:." --add-data="*.ttf:." --add-data="Icon.ico:." Main.PY
   ```

3. 构建结果将位于`dist/HDD-System.app`

4. (可选) 创建DMG文件：
   ```
   brew install create-dmg
   mkdir -p dmg_contents
   cp -r dist/HDD-System.app dmg_contents/
   create-dmg --volname "HDD-System" --volicon "Icon.ico" --window-pos 200 120 --window-size 600 400 --icon "HDD-System.app" 150 190 --app-drop-link 450 190 "HDD-System.dmg" "dmg_contents/"
   ```

## 注意事项

- 确保所有资源文件（图像、音频、字体等）都位于项目根目录
- 构建过程中可能需要互联网连接以下载依赖项
- macOS构建需要在macOS系统上进行，Windows构建需要在Windows系统上进行
- GitHub Actions会自动在适当的环境中构建各平台的可执行程序