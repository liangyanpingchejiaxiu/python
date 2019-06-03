#先去 items定义 再去cmd 里创建 scrapy startproject myproject  再去scrapy shell 网址

# response.body  .headers   response.xpath("//title")   如果要排序 response.xpath('//text [@class='']/text()/a/@href').extract()
#scrapy crawl spider1 -o 导出 items.json 给导出的文件取名 -t类型 json  
