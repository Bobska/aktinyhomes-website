from django.core.management.base import BaseCommand
from main.models import TinyHomeLayout, TinyHomeImage, BlogPost, FAQ


class Command(BaseCommand):
    help = 'Populate the database with content from aktinyhomes.co.nz'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database with Aktiny Homes content...'))
        
        # Clear existing data
        TinyHomeLayout.objects.all().delete()
        TinyHomeImage.objects.all().delete()
        BlogPost.objects.all().delete()
        FAQ.objects.all().delete()
        
        # Create Tiny Home Layouts
        layouts = [
            {
                'name': '6m x 2.4m Tiny Home',
                'description': 'Compact and efficient design perfect for singles or couples. Features open-plan living with loft bedroom.',
                'size': '6m x 2.4m',
                'price_range': 'Contact for pricing'
            },
            {
                'name': '8m x 2.4m Tiny Home',
                'description': 'Popular mid-size option with more space for comfortable living. Includes separate bedroom area.',
                'size': '8m x 2.4m', 
                'price_range': 'Contact for pricing'
            },
            {
                'name': '10m x 3m Tiny Home',
                'description': 'Our largest standard size offering maximum living space and comfort. Perfect for families or those wanting extra room.',
                'size': '10m x 3m',
                'price_range': 'Contact for pricing'
            },
            {
                'name': 'Custom Multi-Unit Build',
                'description': 'Custom designed multi-unit builds for special projects or commercial applications.',
                'size': 'Various sizes available',
                'price_range': 'Custom pricing'
            }
        ]
        
        created_layouts = []
        for layout_data in layouts:
            layout = TinyHomeLayout.objects.create(**layout_data)
            created_layouts.append(layout)
            self.stdout.write(f'Created layout: {layout.name}')
        
        # Create Featured Images from the website
        images = [
            {
                'title': 'Tiny Home Interior - Open Plan Living',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/300179887_355490866665789_1379202795833700960_.jpg/:/rs=w:1023,h:1364',
                'description': 'Beautiful open-plan interior with modern fittings and custom joinery',
                'is_featured': True,
                'layout': created_layouts[0]
            },
            {
                'title': 'Tiny Home Exterior View',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/301047788_1259664138116616_9180614893207849304.jpg',
                'description': 'Sleek exterior design with quality cladding and modern styling',
                'is_featured': True,
                'layout': created_layouts[1]
            },
            {
                'title': 'Custom Kitchen Design',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/432308643_312054858330347_1071125971372559768_.jpg/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:719,h:959',
                'description': 'Custom-designed kitchen with quality appliances and smart storage solutions',
                'is_featured': True,
                'layout': created_layouts[1]
            },
            {
                'title': 'Bedroom Loft Space',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/434414403_1174263284022160_26361300626-1657f42.jpg',
                'description': 'Comfortable loft bedroom with natural lighting and built-in storage',
                'is_featured': True,
                'layout': created_layouts[0]
            },
            {
                'title': 'Living Area with Fireplace',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/432381177_3605057843076251_1492047688754276433.jpg/:/rs=w:719,h:959',
                'description': 'Cozy living area featuring wood-burning fireplace and comfortable seating',
                'is_featured': True,
                'layout': created_layouts[2]
            },
            {
                'title': 'Quality Bathroom Fittings',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/424917009_346762217868543_4201948335848108543_.jpg',
                'description': 'Compact bathroom with quality fittings and smart space utilization',
                'is_featured': True,
                'layout': created_layouts[1]
            },
            {
                'title': 'Outdoor Deck Area',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/426726688_706807144998405_5676824757491673736_.jpg/:/rs=w:719,h:959',
                'description': 'Optional outdoor deck area for extended living space',
                'is_featured': True,
                'layout': created_layouts[2]
            },
            {
                'title': 'Construction Progress - Framing',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/301853860_593485355777409_115156915857900386_n.jpg/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:1023,h:767',
                'description': 'Quality construction showing structural framing and attention to detail',
                'is_featured': True,
                'layout': None
            },
            {
                'title': 'Workshop - Construction in Progress',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/301294499_788485135727789_7414411508054733049_.jpg/:/rs=w:1023,h:1371',
                'description': 'Our workshop where each tiny home is carefully constructed',
                'is_featured': True,
                'layout': None
            },
            {
                'title': 'Multi-Unit Construction Project',
                'image_url': 'https://img1.wsimg.com/isteam/ip/4327e722-b4f0-4d30-8fb1-391b0572724e/300324635_2399096630231715_7414243277109508740.jpg/:/rs=w:1023,h:1364',
                'description': 'Large-scale construction project showing our capability for multi-unit builds',
                'is_featured': True,
                'layout': created_layouts[3]
            }
        ]
        
        for image_data in images:
            image = TinyHomeImage.objects.create(**image_data)
            self.stdout.write(f'Created image: {image.title}')
        
        # Create Blog Posts
        blog_posts = [
            {
                'title': 'Check out our new designs!',
                'content': '''Its the textures, look, Colors and design that's so different, with the simple option of delivery to you flat packed ready to construct yourself. Or we can give our usual full services of build, fit and deliver.

Talk to us about your requirements and we can design something unique for you. Our CNC machine allows us to create custom decorative elements and precise joinery that sets our tiny homes apart.

Whether you're looking for a weekend getaway, a permanent residence, or a rental investment, we have options to suit your needs and budget.'''
            },
            {
                'title': 'CNC At Work - Precision Craftsmanship',
                'content': '''Some Projects and fun with the CNC Machine.

Our new CNC machine has revolutionized the way we approach custom joinery and decorative elements in our tiny homes. The precision and repeatability it offers means we can create intricate designs that would be impossible or extremely time-consuming by hand.

From custom kitchen cabinets to decorative wall panels, the CNC machine allows us to offer personalized touches that make each tiny home unique to its owner.'''
            },
            {
                'title': 'Kitchen Designs - Custom Solutions',
                'content': '''Kitchen Designed, supplied and fitted by A & K Tiny Homes to C & R Builders. These will be available as kit sets, soon to be available on our website shop.

For Tiny Home, Cabins, Caravans. We can design to your specific requirements, ensuring maximum functionality in minimal space. Our kitchens feature:

- Custom cabinetry built to fit your exact space
- Quality appliances sized for tiny home living  
- Smart storage solutions to maximize functionality
- Durable finishes that withstand daily use

Contact us to discuss your kitchen requirements.'''
            },
            {
                'title': 'A Touch Of Precision - New CNC Machine',
                'content': '''Great news here at A & K Tiny Homes, delivery, of our new CNC Machine, now getting set up to provide amazing Carpentry, Cabinets, and carved decorative items to add to our tiny home projects.

This investment in technology allows us to:
- Create precise, repeatable cuts for better quality
- Offer custom decorative elements
- Reduce waste through optimized cutting patterns  
- Provide faster turnaround times on projects

The precision this machine offers will be evident in every tiny home we build going forward.'''
            },
            {
                'title': 'Multi Unit Build Progress - Interior Underway',
                'content': '''Interior of the September Huge project. One of Two 10 x 3mtr Tinys. The Down-lights, Flooring and Fire. Note the Black Windows in this one. The layout is a Tad Different for the New Owners Plans.

This multi-unit build showcases our ability to handle large projects while maintaining attention to detail. Each unit features:
- Custom interior layouts designed for the owners
- Quality LED downlighting throughout
- Engineered flooring for durability
- Wood-burning fireplace for heating
- Black window frames for modern aesthetic

Keep watching for more progress updates on this exciting project!'''
            },
            {
                'title': 'Construction Update - Floor and Walls!',
                'content': '''Time for the Floor to be finished and the Walls going up, cool day to get the lifting and joining done.

The construction process involves careful attention to:
- Structural integrity and building code compliance
- Insulation and weatherproofing
- Precise measurements and square construction
- Quality materials throughout

Each stage is carefully planned and executed to ensure the finished product meets our high standards.'''
            }
        ]
        
        for post_data in blog_posts:
            post = BlogPost.objects.create(**post_data)
            self.stdout.write(f'Created blog post: {post.title}')
        
        # Create FAQs
        faqs = [
            {
                'question': 'Can you add my own designs?',
                'answer': '''Absolutely! We specialize in custom designs tailored to your specific needs and preferences. Our team will work closely with you to understand your vision and create a tiny home that reflects your personal style and functional requirements.

Whether you have detailed plans or just ideas, we can help bring your dream tiny home to life. Our CNC machine and skilled craftsmen allow us to create unique decorative elements and custom joinery that make your home truly one-of-a-kind.''',
                'order': 1
            },
            {
                'question': 'Can these be off-grid?',
                'answer': '''Yes! We offer both on-grid and off-grid options for our tiny homes. Off-grid setups can include:

- Solar panel systems with battery storage
- Composting toilets or septic systems
- Water tanks and pumps
- Propane appliances for cooking and hot water
- Wood-burning stoves for heating

We'll work with you to design a system that meets your off-grid living goals while ensuring comfort and functionality.''',
                'order': 2
            },
            {
                'question': 'How will you handle the scheduling of your work orders?',
                'answer': '''We maintain a production schedule that ensures quality while meeting reasonable timeframes. Each project timeline depends on:

- Complexity of the design
- Custom features requested
- Material availability
- Weather conditions (for construction phases)

During our initial consultation, we'll provide you with a realistic timeline for your project and keep you updated throughout the construction process. We believe in clear communication and will notify you of any changes to the schedule as soon as they arise.''',
                'order': 3
            },
            {
                'question': 'Do you install wood burning stoves?',
                'answer': '''Yes, we can install wood-burning stoves in our tiny homes. Wood stoves are an excellent heating option for tiny homes, providing:

- Efficient heating for small spaces
- Independence from electrical heating systems
- Cozy ambiance and focal point
- Suitable for off-grid living

We ensure all installations meet building codes and safety requirements, including proper clearances, fireproof surrounds, and appropriate ventilation systems. Our team is experienced with various stove types and can recommend the best option for your tiny home size and layout.''',
                'order': 4
            },
            {
                'question': 'What sizes are available?',
                'answer': '''We offer several standard sizes to choose from:

- 6m x 2.4m - Perfect for singles or couples
- 8m x 2.4m - Popular mid-size option
- 10m x 3m - Our largest standard size
- Custom sizes available upon request

Each size can be customized with different layouts and features to maximize the use of space according to your specific needs.''',
                'order': 5
            },
            {
                'question': 'What about building consents and regulations?',
                'answer': '''We're experienced with New Zealand building regulations and can guide you through the consent process. Requirements vary by council and intended use:

- Some tiny homes may qualify as vehicles and not require building consent
- Permanent installations typically require consent
- We can design to meet Building Code requirements
- We assist with documentation for certification

Contact us to discuss the regulatory requirements for your specific situation and location.''',
                'order': 6
            }
        ]
        
        for faq_data in faqs:
            faq = FAQ.objects.create(**faq_data)
            self.stdout.write(f'Created FAQ: {faq.question}')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with Aktiny Homes content!'))
        self.stdout.write(f'Created {TinyHomeLayout.objects.count()} layouts')
        self.stdout.write(f'Created {TinyHomeImage.objects.count()} images')
        self.stdout.write(f'Created {BlogPost.objects.count()} blog posts')
        self.stdout.write(f'Created {FAQ.objects.count()} FAQs')
