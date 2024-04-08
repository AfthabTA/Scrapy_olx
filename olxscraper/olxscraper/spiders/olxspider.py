import scrapy

class olxspider(scrapy.Spider):
    name = 'olx'
    start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self,response):
        
        for products in response.css('li._1DNjI'):
            link=products.css('a._2cbZ2').attrib['href']
            if link is not None:
                yield response.follow(link)

                yield {
                    'name': products.css('span._1hJph::text').get(),

                    'price': products.css('span.T8y-z::text').get().replace('₹',''),

                    'location': products.css('span._1RkZP::text').get(),
                    

                }
            
