from django.core.management.base import BaseCommand
from Home.models import Slider

class Command(BaseCommand):
    help = 'Creates Slider objects'

    def handle(self, *args, **options):
        slider = [
            {
                'id' : 1,
                'title' : "Men's",
                'collection' : 'Collections',
                'year' : 2025,
                'description' : 'Discover the latest fashion trends with our new arrivals. From chic dresses to stylish jackets, find everything you need to refresh your wardrobe with modern, on-trend pieces that suit every occasion.',
                'image' : 'https://res.cloudinary.com/djpt59lvm/image/upload/v1763132585/1-Photoroom_ulwxyn.png',
                'status' : 'active',
            },
            {
                'id': 2,
                'title': "Women's",
                'collection': 'Collections',
                'year': 2025,
                'description': "Make a statement at your next event with our stunning collection of elegant evening wear. Featuring sophisticated gowns, tailored suits, and accessories, you'll find the perfect outfit to shine all night long.",
                'image': 'https://res.cloudinary.com/djpt59lvm/image/upload/v1763132582/2-Photoroom_hf3u64.png',
                'status' : 'active',
            },
            {
                'id': 3,
                'title': "Women's",
                'collection': 'Collections',
                'year': 2025,
                'description': "Effortlessly stylish, our casual chic collection brings together comfort and trend. From laid-back tees to flattering jeans and comfy sneakers, discover versatile pieces that are perfect for everyday wear.",
                'image': 'https://res.cloudinary.com/djpt59lvm/image/upload/v1763132613/6-Photoroom_zgvd9o.png',
                'status': 'active',
            },
            {
                'id': 4,
                'title': "Women's",
                'collection': 'Collections',
                'year': 2025,
                'description': "Complete your look with bold and eye-catching accessories. Explore our range of statement jewelry, scarves, bags, and hats that add the finishing touch to any outfit, making you stand out in style.",
                'image': 'https://res.cloudinary.com/djpt59lvm/image/upload/v1763132584/3-Photoroom_o3a5zx.png',
                'status': 'active',
            },
            {
                'id': 5,
                'title': "Women's",
                'collection': 'Collections',
                'year': 2025,
                'description': "Make a statement at your next event with our stunning collection of elegant evening wear. Featuring sophisticated gowns, tailored suits, and accessories, you'll find the perfect outfit to shine all night long.",
                'image': 'https://res.cloudinary.com/djpt59lvm/image/upload/v1763132583/5-Photoroom_cwts4m.png',
                'status': 'active',
            },
            {
                'id': 6,
                'title': "Women's",
                'collection': 'Collections',
                'year': 2025,
                'description': "Get your hands on our exclusive limited edition pieces. With unique designs and limited availability, these pieces are perfect for those looking to stand out and add something truly special to their wardrobe.",
                'image': 'https://res.cloudinary.com/djpt59lvm/image/upload/v1763132582/4-Photoroom_obl6wp.png',
                'status': 'active',
            },
        ]
        # for s in slider:
        #     if not Slider.objects.filter(id = s['id']).exists() :
        #         Slider.objects.create(**s)
        #         print("Static sliders inserted successfully!")
        #     else:
        #         print(f"Duplicate slider found in ID : {s['id']}")
        #
        for s in slider:
            slider_id = s.get('id')

            # Update or create
            Slider.objects.update_or_create(
                id=slider_id,
                defaults=s
            )

            print(f"Slider with ID {slider_id} has been created/updated successfully!")


