# 百度千帆API技能 for iFlow CLI

百度千帆API工具集，提供智能搜索、百度搜索、百度百科、热榜查询、商品营销文案、PPT生成等多种AI能力。

## 功能列表

| 功能 | 命令 | 说明 |
|------|------|------|
| 智能搜索生成 | `smart_search` | AI增强的智能搜索 |
| 百度搜索 | `baidu_search` | 纯百度搜索 |
| 高性能版智能搜索 | `smart_search_pro` | 高性能智能搜索 |
| 百度百科 | `baike` | 百科词条查询 |
| 百度学术检索 | `academic` | 学术论文检索 |
| 垂类热榜查询 | `category_hot` | 分类热榜 |
| 热榜榜单查询 | `hot_list` | 热门榜单 |
| 商品营销文案 | `product_copy` | 商品文案生成 |
| 商品标题生成 | `product_title` | 商品标题生成 |

## 安装方式

### 方式一：复制文件（推荐）

1. 克隆本仓库到本地：
```bash
git clone https://github.com/dd2673/GQD2.git
cd GQD2
```

2. 复制技能文件夹到 iFlow CLI 的 skills 目录：
```bash
# Windows
xcopy /E /I baidu-qianfan %USERPROFILE%\.iflow\skills\baidu-qianfan

# Linux/Mac
cp -r baidu-qianfan ~/.iflow/skills/baidu-qianfan
```

3. 重启 iFlow CLI 即可使用

### 方式二：手动创建

1. 在 iFlow CLI 的 skills 目录下创建 `baidu-qianfan` 文件夹
2. 创建以下文件：
   - `SKILL.md` - 技能定义
   - `_meta.json` - 元数据
   - `EXAMPLES.md` - 使用示例
   - `scripts/qianfan.py` - API调用脚本
3. 重启 iFlow CLI

## 使用示例

```
baidu_search "Python教程"
baike "刘德华"
academic "人工智能"
hot_list
category_hot "美食"
product_title "iPhone 16 Pro"
```

## API 配置

替换你的apikep

如需更换 API Key，编辑 `scripts/qianfan.py` 中的 `API_KEY` 变量。

## API 文档

- [百度千帆平台](https://cloud.baidu.com/doc/qianfan/index.html)
- [智能搜索API](https://cloud.baidu.com/doc/qianfan-api/s/Hmbu8m06u)
- [百度搜索API](https://cloud.baidu.com/doc/qianfan-api/s/Wmbq4z7e5)

## 许可证

MIT License
