import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

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
            
class olxspider(CrawlSpider):
        name = 'olx'
        start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

        rules =(
                Rule(LinkExtractor(allow='item'),callback='parse_item'),
        )

        def parse_item(self,response):
           

                yield{
                        'property_name': response.css('h1._1hJph::text').get(),

                        'property_id': response.css('div._1-oS0 strong::text')[-1].get(),

                        'breadcrumbs': response.css('ol.rui-2Pidb li a::text').getall(),

                        'price': response.css('span.T8y-z::text').get(),

                        'image_url': response.css('img._1Iq92').attrib['src'],

                        'description': response.xpath('//div[@data-aut-id="itemDescriptionContent"]/p/text()').getall(),

                        'seller_name': response.css('div.eHFQs::text').get(),

                        'location': response.css('span._1RkZP::text').get(),

                        'property_type': response.xpath('//span[@data-aut-id="value_type"]/text()').get(),

                        'bathrooms': response.xpath('//span[@data-aut-id="value_bathrooms"]/text()').get(),

                        'bedrooms': response.xpath('//span[@data-aut-id="value_rooms"]/text()').get(),
                        

                        
                }