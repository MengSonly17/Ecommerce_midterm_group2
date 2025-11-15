from django.core.management.base import BaseCommand
from Home.models import Product

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        products = [
            {
                "name": "Cropped Fitted T-Shirts",
                "description": "Cropped fitted t-shirt featuring short sleeves with embroidery design printed at left chest and crew-neck.",
                "price": 0.025,
                "image": "v1763135128/ZANDO30.06.20250663_dlgwpg.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Wide Leg Denim Jean",
                "description": "Wide leg denim jean featuring side pockets with front button and zipper-up fastening.",
                "price": 0.025,
                "image": "v1763135122/Untitled_Session0045_plj2db.jpg",
                "rate": 3.7,
                "discount_price": 7.49,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Midi Skirt",
                "description": "Midi skirt featuring tie detail with zipper-up fastening at left waist.",
                "price": 0.025,
                "image": "v1763131995/ZD__3937_m1w0os.jpg",
                "rate": 3.7,
                "discount_price": 21.59,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Regular Stripped Shirt",
                "description": "Regular stripped shirt featuring long sleeves with pockets at left chest, shirt collar and front button fastening.",
                "price": 0.025,
                "image": "v1763131997/ZD__4559_wtvtpf.jpg",
                "rate": 3.7,
                "discount_price": 15.95,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Oversized T-Shirts",
                "description": "Oversized t-shirt featuring short sleeves design with printed and round neck.",
                "price": 0.025,
                "image": "v1763131994/ZD__3874_cxeij0.jpg",
                "rate": 3.7,
                "discount_price": 8.37,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Long Sleeves Shirt",
                "description": "Cropped shirt featuring long sleeves, no design printed shirt collar and front button fastening.",
                "price": 0.025,
                "image": "v1763131995/ZD__3852_x14l9w.jpg",
                "rate": 3.7,
                "discount_price": 11.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Regular T-Shirts",
                "description": "Regular t-shirts featuring short sleeves and round neck.",
                "price": 0.025,
                "image": "v1763131996/ZD__4045_ytm8jz.jpg",
                "rate": 3.7,
                "discount_price": 8.96,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Knitted Polo Shirt",
                "description": "Regular knitted polo shirt featuring short sleeves, shirt collar and front button fastening.",
                "price": 0.025,
                "image": "v1763131994/ZD__3592_qjjpu4.jpg",
                "rate": 3.7,
                "discount_price": 13.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Wide Leg Trousers",
                "description": "Wide leg trousers featuring side pockets with front tie adjustable and zipper-up fastening.",
                "price": 0.025,
                "image": "v1763131993/ZD__3504_j8dbac.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Mini Polo Dresses",
                "description": "Mini polo dresses featuring short sleeves, do design printed shirt collar and front button fastening.",
                "price": 0.025,
                "image": "v1763131995/ZD__3880_wrzvg5.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Cropped Long Sleeves Shirt",
                "description": "Cropped shirt featuring long sleeves with front pockets, shirt collar and front buttom fastening.",
                "price": 0.025,
                "image": "v1763131996/ZD__4278_rqp3qm.jpg",
                "rate": 3.7,
                "discount_price": 21.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Poizen Ragen Top",
                "description": "Poizen reagen top featuring sleeveless with front zipper-up fastening and side tie adjustable.",
                "price": 0.025,
                "image": "v1763134845/TAKK0646-Edit_vnq1an.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Tank Top",
                "description": "Tank top featuring sleeveless.",
                "price": 0.025,
                "image": "v1763131993/ZD__2297_xm9d32.jpg",
                "rate": 3.7,
                "discount_price": 5.12,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Off-Shoulder T-Shirts",
                "description": "Off-shoulder t-shirts featuring short sleeves and front printed.",
                "price": 0.025,
                "image": "v1763131993/ZD__1662_lt1oqj.jpg",
                "rate": 3.7,
                "discount_price": 33.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Textured T-Shirts",
                "description": "Cropped textured t-shirts featuring short sleeves and round neck.",
                "price": 0.025,
                "image": "v1763131993/ZD__1725_cnebdw.jpg",
                "rate": 3.7,
                "discount_price": 8.95,
                "quantity": 10,
                "category_id": 1
            },












    {
        "name": "Classic Cotton T-Shirt",
        "description": "A timeless and comfortable t-shirt made from 100% premium cotton. Perfect for everyday wear.",
        "price": 0.025,
        "image": "v1759862273/LEAD_569ZE10_600copy_hwu23h.webp",
        "rate": 3.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 1
    },
    {
        "name": "Slim-Fit Denim Jeans",
        "description": "Modern and stylish slim-fit jeans crafted from high-quality denim. A versatile addition to any wardrobe.",
        "price": 0.045,
        "image": "v1759862296/BEST-MENS-JEANS-2048px-9811_jy0guh.webp",
        "rate": 4.1,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 2
    },
    {
        "name": "Cozy Wool Sweater",
        "description": "Stay warm and fashionable with this cozy sweater made from a soft wool blend. Ideal for chilly days.",
        "price": 0.035,
        "image": "v1759862296/coosh9-222186-min__preview_sl3oqb.jpg",
        "rate": 3.9,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Leather Biker Jacket",
        "description": "A classic biker jacket made from genuine leather. Adds a touch of edge to any outfit.",
        "price": 0.050,
        "image": "v1759862296/WEASLEY-BLCK-0047h-scaled_ngtwa7.jpg",
        "rate": 4.6,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Casual Linen Shirt",
        "description": "A lightweight and breathable linen shirt, perfect for a relaxed and casual look.",
        "price": 0.045,
        "image": "v1759862296/untitled-session3537_rndwei.webp",
        "rate": 4.6,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Tailored Chino Pants",
        "description": "Versatile and stylish chino pants that can be dressed up or down for any occasion.",
        "price": 0.050,
        "image": "v1759862297/chino-page-man-wearing-light-khaki-chino-steps-down-the-stairs-3-e1649749357223-975x1300_vbnlp7.jpg",
        "rate": 3.1,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 6
    },
    {
        "name": "Graphic Print Hoodie",
        "description": "A comfortable and stylish hoodie with a unique graphic print. Perfect for a streetwear look.",
        "price": 0.045,
        "image": "v1759862297/Hustle_1_cycwst.webp",
        "rate": 4.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 7
    },
    {
        "name": "Formal Dress Shirt",
        "description": "A crisp and elegant dress shirt, perfect for formal events and business meetings.",
        "price": 0.050,
        "image": "v1759862297/s7-1390091_alternate4_yvrr6b.avif",
        "rate": 4.2,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Cargo Shorts",
        "description": "Comfortable and practical cargo shorts with multiple pockets. Ideal for outdoor activities.",
        "price": 0.045,
        "image": "v1759862297/1098935_uz1jna.jpg",
        "rate": 3.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 8
    },
    {
        "name": "V-Neck Sweater",
        "description": "A classic v-neck sweater made from a soft and comfortable merino wool.",
        "price": 0.045,
        "image": "v1759862313/il_fullxfull.2663518508_odxm_gnogxi.webp",
        "rate": 4.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Polo Shirt",
        "description": "A classic polo shirt for a smart-casual look.",
        "price": 0.040,
        "image": "v1759862318/mens-blue-mercerised-jersey-polo-shirt-mtpomeblu_1_imph25.webp",
        "rate": 4.2,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Bomber Jacket",
        "description": "A stylish and versatile bomber jacket.",
        "price": 0.050,
        "image": "v1759862318/best-bomber-jackets-654a645c613dd_nljzpk.avif",
        "rate": 3.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Turtleneck Sweater",
        "description": "A warm and stylish turtleneck sweater.",
        "price": 0.050,
        "image": "v1759862319/87010605_08_vlozlu.avif",
        "rate": 3.6,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Denim Jacket",
        "description": "A timeless denim jacket for a casual look.",
        "price": 0.050,
        "image": "v1759862319/87080596_TM_ror0fp.avif",
        "rate": 4.1,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Flannel Shirt",
        "description": "A comfortable and warm flannel shirt.",
        "price": 0.045,
        "image": "v1759862319/MERGED_0073_Layer130_hslfjt.webp",
        "rate": 4.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Pea Coat",
        "description": "A classic and warm pea coat for cold weather.",
        "price": 0.050,
        "image": "v1759862328/PeacoatBoardwalkLSMOBILE1_e399cef2-e10a-4a7d-8c62-3f7ab7f1e6e5_k3stkb.webp",
        "rate": 3.0,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Henley Shirt",
        "description": "A stylish and comfortable henley shirt.",
        "price": 0.045,
        "image": "v1759862328/Ms-LS-Henley-Fog-WOOLLY_4673_tsn0tf.webp",
        "rate": 3.9,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Cardigan Sweater",
        "description": "A versatile and stylish cardigan sweater.",
        "price": 0.045,
        "image": "v1759862249/71m5o8kBjaL._UY350__vvio22.jpg",
        "rate": 3.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Windbreaker Jacket",
        "description": "A lightweight and water-resistant windbreaker jacket.",
        "price": 0.045,
        "image": "v1759862249/womens-windbreaker-jacket-neon-coral-jacket-aviator-nation-684000_idnpa1.webp",
        "rate": 3.4,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Straight-Leg Jeans",
        "description": "Classic straight-leg jeans for a timeless look.",
        "price": 0.045,
        "image": "v1759862250/JORDYN_HIGH_WAISTED_STRAIGHT_LEG_JEANS_16.01.24_05_gttfst.webp",
        "rate": 3.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 2
    }
]

        # for p in products:
        #     Product.objects.update_or_create(
        #         name=p.get("name"),  # field used to check duplication
        #         defaults=p  # values to update if exists
        #     )
        #
        # print("Static products inserted/updated successfully!")
        Product.objects.all().delete()
        for p in products:
            if not Product.objects.filter(name = "dksjf").exists():
                Product.objects.create(**p)
            else :
                print("Duplicate product found")

        print("Static products inserted successfully!")



        # for p in products:
        #     Product.objects.update_or_create(
        #         name=p.get("name"),
        #         defaults=p
        #     )
        #
        # print("Static products inserted/updated successfully!")

        # for s in products:
        #     id = s.get('id')
        #
        #     # Update or create
        #     Product.objects.update_or_create(
        #         id=id,
        #         defaults=s
        #     )
        #     print("Static products inserted successfully!")