from app import app, db
from models import Garage, Service, SparePart, User

# Drop all tables and recreate the database
with app.app_context():
    db.drop_all()
    db.create_all()

def seed_garages(garages_data):
    print(":car: Seeding garages...")
    for garage_data in garages_data:
        garage = Garage(**garage_data)
        db.session.add(garage)
    db.session.commit()
    print("Garage seeding completed.")

def seed_services(services_data):
    print(":wrench: Seeding services...")
    for service_data in services_data:
        service = Service(**service_data)
        db.session.add(service)
    db.session.commit()
    print("Service seeding completed.")

def seed_spare_parts(spare_parts_data):
    print(":nut_and_bolt: Seeding spare parts...")
    for spare_part_data in spare_parts_data:
        spare_part = SparePart(**spare_part_data)
        db.session.add(spare_part)
    db.session.commit()
    print("Spare part seeding completed.")

def seed_users(users_data):
    print(":bust_in_silhouette: Seeding users...")
    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)
    db.session.commit()
    print("User seeding completed.")

if __name__ == '__main__':
    garages_data = [
        {"name": "AutoCare Garage 1", "location": "123 Main Street", "contact_number": "555-111-1111"},
        {"name": "CarFix Center 2", "location": "456 Oak Street", "contact_number": "555-222-2222"},
        {"name": "Quick Tune-Up 3", "location": "789 Pine Street", "contact_number": "555-333-3333"},
        {"name": "Speedy Repairs 4", "location": "321 Elm Street", "contact_number": "555-444-4444"},
        {"name": "Precision Auto 5", "location": "654 Birch Street", "contact_number": "555-555-5555"},
        {"name": "Gearheads Garage 6", "location": "987 Maple Street", "contact_number": "555-666-6666"},
        {"name": "Driveway Doctors 7", "location": "135 Cedar Street", "contact_number": "555-777-7777"},
        {"name": "Road Ready Repairs 8", "location": "246 Spruce Street", "contact_number": "555-888-8888"},
        {"name": "Fast Lane Autos 9", "location": "579 Oakwood Street", "contact_number": "555-999-9999"},
        {"name": "Motor Masters 10", "location": "864 Pinehurst Street", "contact_number": "555-101-0101"}
    ]

    services_data = [
    {"name": "Oil Change", "description": "Regular oil change service", "price": 50.0, "garage_id": 1},
    {"name": "Brake Inspection", "description": "Thorough brake system inspection", "price": 30.0, "garage_id": 2},
    {"name": "Tire Rotation", "description": "Rotating tires for even wear", "price": 25.0, "garage_id": 3},
    {"name": "Battery Replacement", "description": "Install a new car battery", "price": 80.0, "garage_id": 4},
    {"name": "Air Filter Replacement", "description": "Replace the engine air filter", "price": 15.0, "garage_id": 5},
    {"name": "Wheel Alignment", "description": "Aligning wheels for optimal performance", "price": 40.0, "garage_id": 6},
    {"name": "Coolant Flush", "description": "Flush and replace the coolant", "price": 60.0, "garage_id": 7},
    {"name": "Transmission Fluid Change", "description": "Changing transmission fluid", "price": 75.0, "garage_id": 8},
    {"name": "Spark Plug Replacement", "description": "Install new spark plugs", "price": 20.0, "garage_id": 9},
    {"name": "Suspension System Check", "description": "Inspect and assess suspension components", "price": 35.0, "garage_id": 10},
    ]


    spare_parts_data = [
    {"name": "Brake Pads", "description": "High-quality brake pads", "price": 30.0, "image": "https://auto-xpress.co.ke/wp-content/uploads/Web-Blog-Images_Fremax.jpg", "service_id": 2},
    {"name": "Engine Oil Filter", "description": "Premium engine oil filter", "price": 10.0, "image": "https://media.noria.com/sites/Uploads/2018/1/24/6c5f2360-9d80-4dd0-80ce-7ee45300f431_oil-filter-xl_extra_large.jpeg", "service_id": 1},
    {"name": "Air Filter", "description": "Replacement air filter", "price": 15.0, "image": "https://m.media-amazon.com/images/I/71MU4YvtQAL.jpg", "service_id": 5},
    {"name": "Battery", "description": "Car battery replacement", "price": 50.0, "image": "https://cdn.media.halfords.com/i/washford/950303/Halfords-HCB063-Calcium-12V-Car-Battery-4-Year-Guarantee?fmt=auto&qlt=default&$sfcc_tile$&w=680", "service_id": 2},
    {"name": "Wiper Blades", "description": "Windshield wiper blade set", "price": 12.0, "image": "https://cmhvolvocars.co.za/wp-content/uploads/2021/10/CMH-Volvo-Cars-Bryanston-Windscreen-Wiper-Blades-scaled.webp", "service_id": 3},
    {"name": "Spark Plugs", "description": "Set of spark plugs", "price": 8.0, "image": "https://m.media-amazon.com/images/I/91vr2G7nM2L.jpg", "service_id": 3},
    {"name": "Brake Fluid", "description": "Quality brake fluid", "price": 20.0, "image": "https://pfc.parts/wp-content/uploads/2013/05/Brake-Fluids-sm.png", "service_id": 10},
    {"name": "Transmission Filter Kit", "description": "Transmission filter and gasket kit", "price": 25.0, "image": "https://www.onestopautogarage.co.ke/wp-content/uploads/2023/07/transmission_filter-removebg-preview.png", "service_id": 8},
    {"name": "Cabin Air Filter", "description": "Interior cabin air filter", "price": 18.0, "image": "https://www.fram.com/media/wysiwyg/products/FRAM-Web-cabinfilters_recolored.png", "service_id": 5},
    {"name": "Fuel Pump", "description": "Electric fuel pump", "price": 40.0, "image": "https://m.media-amazon.com/images/I/61Rpj0vTgZL._AC_SL1419_.jpg", "service_id": 4},
    {"name": "Oxygen Sensor", "description": "Engine oxygen sensor", "price": 30.0, "image": "https://www.densoautoparts.com/wp-content/uploads/2022/10/Oxygen-Sensor2-web.png", "service_id": 6},
    {"name": "Radiator Cap", "description": "High-pressure radiator cap", "price": 7.0, "image": "https://www.deepperformance.com/web/image/product.template/67994/image_1024?unique=36fe552", "service_id": 6},
    {"name": "Power Steering Fluid", "description": "Power steering fluid", "price": 15.0, "image": "https://lubrex.net/wp-content/uploads/2022/01/Power-Steering-Fluid.webp", "service_id": 7},
    {"name": "Wheel Bearing Kit", "description": "Wheel bearing replacement kit", "price": 22.0, "image": "https://api.rotobox-wheels.com/storage/cache/ce/ceramic-bearings-for-one-wheel-36955edab50d5b84069cfee0a5b1aeef.png", "service_id": 7},
    {"name": "Timing Belt Kit", "description": "Timing belt and tensioner kit", "price": 35.0, "image": "https://m.media-amazon.com/images/I/81RW9fd3tJL._AC_UF894,1000_QL80_.jpg", "service_id": 4},
    {"name": "Thermostat", "description": "Engine thermostat", "price": 10.0, "image": "https://haynes.com/en-gb/sites/default/files/styles/opengraph/public/Car_thermostat_412151692.jpg?itok=00oA1VfA", "service_id": 8},
    {"name": "Starter Motor", "description": "Car starter motor", "price": 45.0, "image": "https://i.ytimg.com/vi/kFsl5r34lCI/maxresdefault.jpg", "service_id": 9},
    {"name": "Alternator", "description": "Automotive alternator", "price": 55.0, "image": "https://www.shutterstock.com/image-illustration/automotive-power-generating-alternator-generator-600nw-2354627443.jpg", "service_id": 9},
    {"name": "CV Joint Kit", "description": "CV joint and boot kit", "price": 30.0, "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fgrandmark.co.za%2Fsolid-cv-joints%2F&psig=AOvVaw1AqRmZtQfoIvnJ1ehRRL9C&ust=1706106964897000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJjS0PXd84MDFQAAAAAdAAAAABAG", "service_id": 10},
    {"name": "Fuel Filter", "description": "Fuel filter replacement", "price": 12.0, "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.supercheapauto.co.nz%2Fp%2Fryco-ryco-universal-fuel-filter---z4%2F621689.html&psig=AOvVaw3OJt-CrsPVNKr0yiapg2BT&ust=1706107056324000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJDa-Jre84MDFQAAAAAdAAAAABAM", "service_id": 1},
    ]
    
    users_data = [
    {"username": "Craig", "email": "Craig@gmail.com", "password_hash": "hashed_password1"},
    {"username": "Claire", "email": "Claire@gmail.com", "password_hash": "hashed_password2"},
    {"username": "Ivy", "email": "Ivy@gmail.com", "password_hash": "hashed_password3"},
    {"username": "Dennis", "email": "Dennis@gmail.com", "password_hash": "hashed_password4"},
    {"username": "Guyo", "email": "Guyo@gmail.com", "password_hash": "hashed_password5"},
    {"username": "Leroy", "email": "Leroy@gmail.com", "password_hash": "hashed_password6"},
    {"username": "Anita", "email": "Anita@gmail.com", "password_hash": "hashed_password7"},
    {"username": "jared", "email": "Jared@gmail.com", "password_hash": "hashed_password8"},
    {"username": "Davie", "email": "Davie@gmail.com", "password_hash": "hashed_password9"},
    {"username": "Mitchell", "email": "Mitchell@gmail.com", "password_hash": "hashed_password10"},
    ]


    with app.app_context():
        seed_garages(garages_data)
        seed_services(services_data)
        seed_spare_parts(spare_parts_data)
        seed_users(users_data)