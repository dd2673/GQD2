#!/usr/bin/env python3
"""
百度千帆API调用脚本
封装百度千帆平台的多种AI能力

文档参考：
- 智能搜索生成: https://cloud.baidu.com/doc/qianfan-api/s/Hmbu8m06u
- 百度搜索: https://cloud.baidu.com/doc/qianfan-api/s/Wmbq4z7e5
"""

导入argparse
导入json
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from输入import可选，字典，任意，列表

# API配置
API_KEY = "替换为你的API"
BASE_URL = “https://qianfan.baidubce.com”
RATE_LIMIT_DELAY = 0.34  # 3 QPS = 每次请求约0.34秒

# 默认模型
DEFAULT_MODEL = “ernie-4.5-turbo-32k”

# 功能映射
API_FUNCTIONS = {
    “智能搜索”: {
        “名称”: "智能搜索生成",
“每日配额”：100,
        "doc": "https://cloud.baidu.com/doc/qianfan-api/s/Hmbu8m06u",
        "description": "AI增强的智能搜索，传入模型名称时启用"
    },
    "baidu_search": {
        "name": "百度搜索",
        "daily_quota": 1000,
        "doc": "https://cloud.baidu.com/doc/qianfan-api/s/Wmbq4z7e5",
        "description": "纯百度搜索，不传模型名称"
    },
    "smart_search_pro": {
        "name": "高性能版智能搜索生成",
        "daily_quota": 100,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Kmiy99ziv",
        "description": "使用baidu_search_v2的高性能搜索"
    },
    "academic": {
        "name": "百度学术检索",
        "daily_quota": 1000,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Amkw9qpzd",
        "description": "学术论文检索"
    },
    "baike": {
        "name": "百度百科",
        "daily_quota": 1000,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/bmh4stpbh",
        "description": "百科词条查询"
    },
    "baike_entry": {
        "name": "百科词条",
        "daily_quota": 100,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Zmh4stpel",
        "description": "词条详情获取"
    },
    "miaodong": {
        "name": "秒懂百科",
        "daily_quota": 100,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Mmh4stp99",
        "description": "视频百科"
    },
    "star_graph": {
        "name": "百科星图列表查询",
        "daily_quota": 100,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/cmi721sy9",
        "description": "星图数据查询"
    },
    "category_hot": {
        "name": "垂类热榜查询",
        "daily_quota": 10,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Lmhcvvxb2",
        "description": "分类热榜"
    },
    "hot_list": {
        "name": "热榜榜单查询",
        "daily_quota": 10,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Amhcvzqs0",
        "description": "热门榜单"
    },
    "video_note": {
        "name": "视频AI笔记",
        "daily_quota": "10800秒",
        "doc": "https://cloud.baidu.com/doc/qianfan/s/qmhcvrqt4",
        "description": "视频内容提取"
    },
    "product_copy": {
        "name": "智能商品营销文案生成",
        "daily_quota": 10,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Emhcw56e1",
        "description": "商品文案"
    },
    "product_title": {
        "name": "商品生动化标题生成",
        "daily_quota": 10,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/9mhcw5u3y",
        "description": "商品标题"
    },
    "ppt_command": {
        "name": "指令智能生成PPT",
        "daily_quota": 5,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Mmhcvtke6",
        "description": "指令式PPT"
    },
    "ppt_smart": {
        "name": "智能生成PPT",
        "daily_quota": 50,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/4mjcnolh6",
        "description": "智能PPT"
    },
    "similar_image": {
        "name": "相似图搜索",
        "daily_quota": 100,
        "doc": "https://cloud.baidu.com/doc/qianfan/s/Pmir40a3x",
        "description": "图片相似搜索"
    }
}

# 上次请求时间（用于限流）
_last_request_time = 0

def rate_limit():
    """限流控制"""
    global _last_request_time
    current_time = time.time()
    elapsed = current_time - _last_request_time
    if elapsed < RATE_LIMIT_DELAY:
        time.sleep(RATE_LIMIT_DELAY - elapsed)
    _last_request_time = time.time()

def make_request(endpoint: str, params: Dict[str, Any], method: str = "POST", 
                 use_x_appbuilder: bool = True, base_url: str = BASE_URL) -> Dict[str, Any]:
    """
    发送API请求
    
    Args:
        endpoint: API端点
        params: 请求参数
        method: 请求方法 (POST/GET)
        use_x_appbuilder: 是否使用X-Appbuilder-Authorization头
        base_url: 基础URL
        
    Returns:
        API响应
    """
    rate_limit()
    
    url = f"{base_url}{endpoint}"
    
    if use_x_appbuilder:
        headers = {
            "Content-Type": "application/json",
            "X-Appbuilder-Authorization": f"Bearer {API_KEY}"
        }
    else:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    
    if method == "GET":
        # GET请求将参数作为URL查询字符串
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"
        req = urllib.request.Request(url, headers=headers, method='GET')
    else:
        data = json.dumps(params, ensure_ascii=False).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8') if e.fp else str(e)
        return {"error": f"HTTP {e.code}", "details": error_body}
    except urllib.error.URLError as e:
        return {"error": f"URL Error: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def ai_search(query: str, model: Optional[str] = None, stream: bool = False, 
              search_source: str = "baidu_search_v2", enable_deep_search: bool = False) -> Dict[str, Any]:
    """
    智能搜索/百度搜索 API
    
    Args:
        query: 搜索查询
        model: 模型名称，不传则为纯百度搜索
        stream: 是否流式输出
        search_source: 搜索引擎版本 baidu_search_v1 或 baidu_search_v2
        enable_deep_search: 是否开启深度搜索
    """
    endpoint = "/v2/ai_search/chat/completions"
    
    params = {
        "messages": [
            {"role": "user", "content": query}
        ],
        "stream": stream,
        "search_source": search_source,
        "enable_deep_search": enable_deep_search
    }
    
    if model:
        params["model"] = model
    
    return make_request(endpoint, params)

def smart_search(query: str, model: str = DEFAULT_MODEL) -> Dict[str, Any]:
    """智能搜索生成（带模型）"""
    return ai_search(query, model=model, search_source="baidu_search_v2")

def baidu_search(query: str) -> Dict[str, Any]:
    """纯百度搜索（使用专用web_search端点）"""
    endpoint = "/v2/ai_search/web_search"
    
    params = {
        "messages": [
            {"role": "user", "content": query}
        ],
        "search_source": "baidu_search_v2",
        "resource_type_filter": [{"type": "web", "top_k": 10}]
    }
    
    return make_request(endpoint, params)

def smart_search_pro(query: str, model: str = DEFAULT_MODEL) -> Dict[str, Any]:
    """高性能版智能搜索生成"""
    return ai_search(query, model=model, search_source="baidu_search_v2", enable_deep_search=True)

def academic_search(query: str) -> Dict[str, Any]:
    """百度学术检索（使用专用学术API）"""
    endpoint = "/v2/tools/baidu_scholar/search"
    
    params = {
        "wd": query,
        "enable_abstract": True
    }
    
    return make_request(endpoint, params, method="GET")

def baike(query: str) -> Dict[str, Any]:
    """百度百科查询（使用专用百科API）"""
    endpoint = "/v2/baike/lemma/get_content"
    base_url = "https://appbuilder.baidu.com"
    
    params = {
        "search_type": "lemmaTitle",
        "search_key": query
    }
    
    return make_request(endpoint, params, method="GET", base_url=base_url)

def baike_entry(entry_id: str) -> Dict[str, Any]:
    """百科词条详情"""
    # 使用智能搜索查询词条详情
    return ai_search(f"查询百科词条：{entry_id}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def miaodong(query: str) -> Dict[str, Any]:
    """秒懂百科"""
    return ai_search(f"秒懂百科：{query}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def star_graph(theme: str) -> Dict[str, Any]:
    """百科星图列表查询"""
    return ai_search(f"百科星图：{theme}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def category_hot_list(category: str = "美食", media_type: str = "抖音", time_range: int = 1) -> Dict[str, Any]:
    """垂类热榜查询（使用专用热榜API）
    
    Args:
        category: 垂类类型，可选：美食、美妆、汽车（仅这3个值有效）
        media_type: 媒体类型，可选：抖音、小红书
        time_range: 时间范围，可选：1(近一天)、3(近三天)、7(近7天)
    """
    endpoint = "/v2/tools/trending_lists/vertical"
    
    # 映射用户输入的category到API支持的type值
    type_mapping = {
        "美食": "美食",
        "美妆": "美妆", 
        "汽车": "汽车",
        "科技": "汽车",  # 科技映射到汽车
        "数码": "汽车",
        "游戏": "汽车",
        "娱乐": "美食",
        "体育": "汽车",
        "财经": "汽车"
    }
    
    type_value = type_mapping.get(category, "美食")  # 默认使用美食
    
    params = {
        "type": type_value,
        "mediaType": media_type,
        "timeRange": time_range
    }
    
    return make_request(endpoint, params)

def hot_list(platform_type: int = 6) -> Dict[str, Any]:
    """热榜榜单查询（使用专用热榜API）
    
    Args:
        platform_type: 平台类型
        2-微博热榜、3-头条热榜、6-抖音热榜、7-知乎热榜、8-B站热榜、
        4-百度热榜、9-贴吧热议榜、10-快手热榜、14-小红书热榜
    """
    endpoint = "/v2/tools/trending_lists/medium"
    
    params = {
        "type": platform_type
    }
    
    return make_request(endpoint, params, method="GET")

def video_ai_note(video_url: str) -> Dict[str, Any]:
    """视频AI笔记"""
    return ai_search(f"总结视频内容：{video_url}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def product_copywriting(product_info: str) -> Dict[str, Any]:
    """智能商品营销文案生成"""
    return ai_search(f"为以下商品生成营销文案：{product_info}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def product_title(product_info: str, num: str = None, img_urls: List[str] = None) -> Dict[str, Any]:
    """商品生动化标题生成（使用专用电商API）
    
    Args:
        product_info: 商品名称
        num: 商品货号(可选)
        img_urls: 商品图片URL列表(可选)
    """
    endpoint = "/v2/tools/e_commerce/generate_titles"
    
    params = {
        "stream": False,
        "parameters": {
            "full_product_name": product_info
        }
    }
    
    if num:
        params["parameters"]["num"] = num
    if img_urls:
        params["parameters"]["img"] = img_urls
    
    return make_request(endpoint, params)

def ppt_command(command: str) -> Dict[str, Any]:
    """指令智能生成PPT"""
    return ai_search(f"生成PPT大纲：{command}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def ppt_smart(topic: str) -> Dict[str, Any]:
    """智能生成PPT"""
    return ai_search(f"为以下主题生成PPT内容：{topic}", model=DEFAULT_MODEL, search_source="baidu_search_v2")

def similar_image(image_url: str) -> Dict[str, Any]:
    """相似图搜索"""
    return ai_search(f"搜索相似图片：{image_url}", model=None, search_source="baidu_search_v2")

def list_functions():
    """列出所有可用功能"""
    print("\n百度千帆API可用功能列表：")
    print("=" * 70)
    for func_name, info in API_FUNCTIONS.items():
        print(f"\n  {func_name}")
        print(f"    名称: {info['name']}")
        print(f"    配额: {info['daily_quota']}")
        print(f"    说明: {info['description']}")
    print("\n" + "=" * 70)
    print(f"\nAPI Key: {API_KEY[:20]}...")
    print(f"速率限制: 3 QPS")
    print(f"默认模型: {DEFAULT_MODEL}")

def extract_content(result: Dict[str, Any]) -> str:
    """从API响应中提取内容"""
    if "error" in result:
        return f"错误: {result.get('error')}\n详情: {result.get('details', '')}"
    
    if "choices" in result and len(result["choices"]) > 0:
        message = result["choices"][0].get("message", {})
        return message.get("content", "无内容")
    
    return json.dumps(result, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(
        description="百度千帆API调用工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python qianfan.py smart_search "人工智能发展趋势"
  python qianfan.py baidu_search "Python 教程"
  python qianfan.py baike "量子计算"
  python qianfan.py hot_list
  python qianfan.py product_copy "智能手表，健康监测功能"
  python qianfan.py list  # 列出所有功能
        """
    )
    
    parser.add_argument("function", help="功能名称")
    parser.add_argument("args", nargs="*", help="功能参数")
    parser.add_argument("--raw", action="store_true", help="输出原始JSON响应")
    
    args = parser.parse_args()
    
    # 列出功能
    if args.function == "list":
        list_functions()
        return
    
    # 功能映射
    function_map = {
        "smart_search": lambda: smart_search(args.args[0] if args.args else ""),
        "baidu_search": lambda: baidu_search(args.args[0] if args.args else ""),
        "smart_search_pro": lambda: smart_search_pro(args.args[0] if args.args else ""),
        "academic": lambda: academic_search(args.args[0] if args.args else ""),
        "academic_search": lambda: academic_search(args.args[0] if args.args else ""),
        "baike": lambda: baike(args.args[0] if args.args else ""),
        "baike_entry": lambda: baike_entry(args.args[0] if args.args else ""),
        "miaodong": lambda: miaodong(args.args[0] if args.args else ""),
        "star_graph": lambda: star_graph(args.args[0] if args.args else ""),
        "category_hot": lambda: category_hot_list(args.args[0] if args.args else ""),
        "hot_list": lambda: hot_list(),
        "video_note": lambda: video_ai_note(args.args[0] if args.args else ""),
        "product_copy": lambda: product_copywriting(args.args[0] if args.args else ""),
        "product_title": lambda: product_title(args.args[0] if args.args else ""),
        "ppt_command": lambda: ppt_command(args.args[0] if args.args else ""),
        "ppt_smart": lambda: ppt_smart(args.args[0] if args.args else ""),
        "similar_image": lambda: similar_image(args.args[0] if args.args else ""),
    }
    
    if args.function not in function_map:
        print(f"错误: 未知功能 '{args.function}'")
        print("使用 'python qianfan.py list' 查看所有可用功能")
        sys.exit(1)
    
    if not args.args and args.function not in ["hot_list", "list"]:
        print(f"错误: 功能 '{args.function}' 需要参数")
        sys.exit(1)
    
    # 执行请求
    func_info = API_FUNCTIONS.get(args.function, {})
    print(f"\n正在调用: {func_info.get('name', args.function)}")
    print("-" * 50)
    
    result = function_map[args.function]()
    
    # 输出结果
    if args.raw:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if "error" in result:
            print(f"\n错误: {result.get('error')}")
            if "details" in result:
                print(f"详情: {result.get('details')}")
        else:
            print("\n" + extract_content(result))
            
            # 显示引用来源
            if "references" in result and result["references"]:
                print("\n" + "-" * 50)
                print("参考来源:")
                for ref in result["references"][:5]:
                    print(f"  - [{ref.get('id', '?')}] {ref.get('title', '未知标题')}")
                    print(f"    {ref.get('url', '')}")

if __name__ == "__main__":
    main()
