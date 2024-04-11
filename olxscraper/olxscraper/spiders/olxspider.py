import scrapy
# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor
import json


# class olxspider(scrapy.Spider):
#     name = 'olx'
#     start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

#     def parse(self,response):
        
#         for products in response.css('li._1DNjI'):
#             link=products.css('a._2cbZ2').attrib['href']
#             if link is not None:
#                 yield response.follow(link)

#                 yield {
#                     'name': products.css('h1._1hJph::text').get(),

#                     'price': products.css('span.T8y-z::text').get().replace('₹',''),

#                     'location': products.css('span._1RkZP::text').get(),
                    

#                 }

# https://www.olx.in/item/sree-pottammal-iid-1764531561
# https://www.olx.in/item/3bhk-luxury-furnished-flat-for-rent-at-thondayad-calicut-md-iid-1765792144
            
# class olxspider(CrawlSpider):
#         name = 'olx'

#         allowed_domains=['olx.in']

#         start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

#         headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'}

#         rules =(
#                 Rule(LinkExtractor(allow='item'),callback='parse_item'),
#         )

#         def parse_item(self,response):
           
#                 price=response.css('span.T8y-z::text').get()
#                 if print is not None:
#                         spl_price=price.split()
#                         if len(spl_price)>=2:
#                                 currency=spl_price[0]
#                                 amount=spl_price[-1]
#                                 price_dic={'amount':amount,'currency':currency,}


#                 yield{
#                         'property_name': response.css('h1._1hJph::text').get(),

#                         'propery_id't: response.css('div._1-oS0 strong::text')[-1].get(),

#                         'breadcrumbs': response.css('ol.rui-2Pidb li a::text').getall(),

#                         'price': price_dic,

#                         'image_url': response.xpath('//img[@data-aut-id="defaultImg"]/@src').get(),

#                         'description': response.xpath('//div[@data-aut-id="itemDescriptionContent"]/p/text()').getall(),

#                         'seller_name': response.css('div.eHFQs::text').get(),

#                         'location': response.css('span._1RkZP::text').get(),

#                         'property_type': response.xpath('//span[@data-aut-id="value_type"]/text()').get(),

#                         'bathrooms': response.xpath('//span[@data-aut-id="value_bathrooms"]/text()').get(),

#                         'bedrooms': response.xpath('//span[@data-aut-id="value_rooms"]/text()').get(),
                        

                        
#                 }

#                 page=2
#                 while page<=300:
#                         next_page='https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&platform=web-desktop&relaxedFilters=true&size=40&user=023995345675097202&page={page}'

#                         yield response.follow(next_page, callback=self.parse_item)

# https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page=2&platform=web-desktop&relaxedFilters=true&size=40&user=023995345675097202
# https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page=3&platform=web-desktop&relaxedFilters=true&size=40&user=023995345675097202
# https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page=2     
# https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&platform=web-desktop&relaxedFilters=true&size=40&user=023995345675097202&page=2



class olxspider(scrapy.Spider):
    name = 'olx'

    allowed_domains=['olx.in']

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'}

    start_urls=['https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page=1&platform=web-desktop&relaxedFilters=true&size=40&user=047405430870509113']

    def parse(self,response):
        data=json.loads(response.body)
        
        
        for property in data['data']:
        
            item ={
                'property_name': property['title'],

                'propery_id': property['id'],

                'breadcrumbs': ['Home', 'Properties', 'For Rent: Houses & Apartments', 'For Rent: Houses & Apartments in Kerala', 'For Rent: Houses & Apartments in Kozhikode', 'For Rent: Houses & Apartments in '+property['locations_resolved']['SUBLOCALITY_LEVEL_1_name'],property['title']],

            }
            
            yield item

            next_page= data['metadata']['next_page_url']
        for i in range(0,5):
                next_page=response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)