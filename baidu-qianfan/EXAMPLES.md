# 百度千帆API使用示例

## 快速开始

### 1. 列出所有可用功能
```bash
python ~/.iflow/skills/baidu-qianfan/scripts/qianfan.py list
```

### 2. 智能搜索
```bash
python qianfan.py smart_search "人工智能最新进展"
```

### 3. 百度搜索
```bash
python qianfan.py baidu_search "Python 教程"
```

### 4. 百度百科查询
```bash
python qianfan.py baike "量子计算"
```

### 5. 学术检索
```bash
python qianfan.py academic "大语言模型应用"
```

### 6. 热榜查询
```bash
# 查看热榜榜单
python qianfan.py hot_list

# 查看某分类热榜
python qianfan.py category_hot "科技"
```

### 7. 商品文案生成
```bash
# 营销文案
python qianfan.py product_copy "智能手表，支持心率监测、运动追踪、睡眠分析"

# 商品标题
python qianfan.py product_title "无线蓝牙耳机，主动降噪，续航30小时"
```

### 8. PPT生成
```bash
# 智能生成PPT
python qianfan.py ppt_smart "2025年AI行业发展趋势"

# 指令生成PPT
python qianfan.py ppt_command "创建一份关于新能源汽车市场的分析报告PPT"
```

### 9. 相似图搜索
```bash
python qianfan.py similar_image "https://example.com/image.jpg"
```

## 在对话中使用

在iFlow CLI中，可以直接请求使用这些功能：

```
帮我搜索一下最近的人工智能新闻
```

```
查一下"深度学习"的百科内容
```

```
生成一个关于智能家居的营销文案
```

## 注意事项

1. **配额限制**: 注意各功能的每日配额，避免超额使用
2. **速率限制**: 3 QPS，脚本已内置限流控制
3. **网络要求**: 需要能够访问百度千帆API
