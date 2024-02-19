from bs4 import BeautifulSoup
import script.smartphone_class as sc
from yarl import URL
import datetime


def _extract_nb_reviews_V0(soup: BeautifulSoup) -> str:
    nb_reviews = soup.find("span", attrs={"class": "rating__count"}).text
    return nb_reviews


def _extract_stars_V0(soup: BeautifulSoup) -> str:
    stars = str(soup.find("a", attrs={"class": "rating"}))
    return stars


def _extract_price_V0(soup: BeautifulSoup) -> str:
    price = soup.find("p", attrs={"class": "price__amount"}).text.strip()
    return price


def _extract_image(soup: BeautifulSoup) -> str:
    """Permet d'obtenir l'image du téléphone grâce à une URL paramétrable."""
    try:
        url = soup.find("img", attrs={"class": "complementary-push__main-image"})["src"]
    except TypeError:
        url = soup.find("img", attrs={"class": "product-viewer__placeholder-img"})[
            "src"
        ]
    index_to_slice = url.find("&resMode")
    img = url[:index_to_slice]
    url_img = URL(img)
    final_url_img = str(url_img.with_query("wid=2000&hei=2000"))
    return final_url_img


def _extract_scraped_day() -> str:
    return str(datetime.datetime.now())


def extract_features(soup: BeautifulSoup) -> dict:
    span_elements = soup.find_all("span", class_="is--medium")
    keys = [span_element.text[:-2] for span_element in span_elements]
    # on retire les 2 caractères " :" pour faire les clés du futur dictionnaire
    keys.extend(["Prix", "Etoiles", "Commentaires", "Image", "ScrapingTime"])

    feature_values = list()
    for span_element in span_elements:
        feature_values.append(str(span_element.find_next_sibling(text=True)).strip())

    feature_values.extend(
        [
            _extract_price_V0(soup),
            _extract_stars_V0(soup),
            _extract_nb_reviews_V0(soup),
            _extract_image(soup),
            _extract_scraped_day(),
        ]
    )

    characteristics = {column: feature for column, feature in zip(keys, feature_values)}
    return characteristics


def extract_model(dict_features: dict):
    try:
        model = dict_features["Modèle"]
    except KeyError:
        return None
    else:
        return model


def extract_color(dict_features: dict):
    try:
        color = dict_features["Couleur"]
    except KeyError:
        return None
    else:
        return color


def extract_os(dict_features: dict):
    try:
        os = dict_features["Système d'exploitation"]
    except KeyError:
        return None
    else:
        return os


def extract_sim_type(dict_features: dict):
    try:
        sim_type = dict_features["Type de SIM"]
    except KeyError:
        return None
    else:
        return sim_type


def extract_sim_number(dict_features: dict):
    try:
        sim_number = dict_features["Nombre de SIM"]
    except KeyError:
        return None
    else:
        return sim_number


def extract_cpu(dict_features: dict):
    try:
        cpu = dict_features["Processeur"]
    except KeyError:
        return None
    else:
        return cpu


def extract_cpu_details(dict_features: dict):
    try:
        cpu_details = dict_features["Détails du Processeur"]
    except KeyError:
        return None
    else:
        return cpu_details


def extract_battery(dict_features: dict):
    try:
        battery = dict_features["Batterie"]
    except KeyError:
        return None
    else:
        return battery


def extract_charging_type(dict_features: dict):
    try:
        charging_type = dict_features["Type de charge"]
    except KeyError:
        return None
    else:
        return charging_type


def extract_fast_charging(dict_features: dict):
    try:
        fast_charging = dict_features["Charge rapide"]
    except KeyError:
        return None
    else:
        return fast_charging


def extract_screen_size(dict_features: dict):
    try:
        screen_size = dict_features["Taille de l'écran (diagonale, en pouces)"]
    except KeyError:
        return None
    else:
        return screen_size


def extract_screen_tech(dict_features: dict):
    try:
        screen_tech = dict_features["Technologie de l'écran"]
    except KeyError:
        return None
    else:
        return screen_tech


def extract_screen_resolution(dict_features: dict):
    try:
        screen_resolution = dict_features["Résolution de l'écran"]
    except KeyError:
        return None
    else:
        return screen_resolution


def extract_screen_type(dict_features: dict):
    try:
        screen_type = dict_features["Type d'écran"]
    except KeyError:
        return None
    else:
        return screen_type


def extract_refresh_rate(dict_features: dict):
    try:
        refresh_rate = dict_features["Fréquence de balayage"]
    except KeyError:
        return None
    else:
        return refresh_rate


def extract_network(dict_features: dict):
    try:
        network = dict_features["Réseau"]
    except KeyError:
        return None
    else:
        return network


def extract_bluetooth(dict_features: dict):
    try:
        bluetooth = dict_features["Bluetooth"]
    except KeyError:
        return None
    else:
        return bluetooth


def extract_wifi(dict_features: dict):
    try:
        wifi = dict_features["Norme Wifi"]
    except KeyError:
        return None
    else:
        return wifi


def extract_usb_type_c(dict_features: dict):
    try:
        usb_type_c = dict_features["Port USB Type-C"]
    except KeyError:
        return None
    else:
        return usb_type_c


def extract_storage(dict_features: dict):
    try:
        storage = dict_features["Mémoire interne"]
    except KeyError:
        return None
    else:
        return storage


def extract_upgrade_storage(dict_features: dict):
    try:
        upgrade_storage = dict_features["Extension de la mémoire"]
    except KeyError:
        return None
    else:
        return upgrade_storage


def extract_ram(dict_features: dict):
    try:
        ram = dict_features["Mémoire RAM"]
    except KeyError:
        return None
    else:
        return ram


def extract_sensor(dict_features: dict):
    try:
        sensor = dict_features["Nombre de capteurs"]
    except KeyError:
        return None
    else:
        return sensor


def extract_sensor_resolution(dict_features: dict):
    try:
        sensor_resolution = dict_features["Résolution"]
    except KeyError:
        return None
    else:
        return sensor_resolution


def extract_repairability_index(dict_features: dict):
    try:
        repairability_index = dict_features["Indice de réparabilité"]
    except KeyError:
        return None
    else:
        return repairability_index


def extract_warranty(dict_features: dict):
    try:
        warranty = dict_features["Garantie"]
    except KeyError:
        return None
    else:
        return warranty


def extract_made_in(dict_features: dict):
    try:
        made_in = dict_features["Fabriqué en"]
    except KeyError:
        return None
    else:
        return made_in


def extract_brand(dict_features: dict):
    try:
        brand = dict_features["Marque"]
    except KeyError:
        return None
    else:
        return brand


def extract_das_head(dict_features: dict):
    try:
        das_head = dict_features["DAS Tête"]
    except KeyError:
        return None
    else:
        return das_head


def extract_das_chest(dict_features: dict):
    try:
        das_chest = dict_features["DAS Tronc"]
    except KeyError:
        return None
    else:
        return das_chest


def extract_das_limb(dict_features: dict):
    try:
        das_limb = dict_features["DAS Membres"]
    except KeyError:
        return None
    else:
        return das_limb


def extract_height(dict_features: dict):
    try:
        height = dict_features["Hauteur produit"]
    except KeyError:
        return None
    else:
        return height


def extract_width(dict_features: dict):
    try:
        width = dict_features["Largeur produit"]
    except KeyError:
        return None
    else:
        return width


def extract_thickness(dict_features: dict):
    try:
        thickness = dict_features["Epaisseur produit"]
    except KeyError:
        return None
    else:
        return thickness


def extract_net_weight(dict_features: dict):
    try:
        net_weight = dict_features["Poids net"]
    except KeyError:
        return None
    else:
        return net_weight


def extract_price(dict_features: dict):
    try:
        price = dict_features["Prix"]
    except KeyError:
        return None
    else:
        return price


def extract_stars(dict_features: dict):
    try:
        stars = dict_features["Etoiles"]
    except KeyError:
        return None
    else:
        return stars


def extract_reviews(dict_features: dict):
    try:
        reviews = dict_features["Commentaires"]
    except KeyError:
        return None
    else:
        return reviews


def extract_img(dict_features: dict):
    try:
        img = dict_features["Image"]
    except KeyError:
        return None
    else:
        return img


def extract_scraping_time(dict_features: dict):
    try:
        scraping_time = dict_features["ScrapingTime"]
    except KeyError:
        return None
    else:
        return scraping_time


def smartphone_characteristics(dict_features: dict) -> sc.Smartphone:
    model = extract_model(dict_features)
    color = extract_color(dict_features)
    os = extract_os(dict_features)
    sim_type = extract_sim_type(dict_features)
    sim_number = extract_sim_number(dict_features)
    cpu = extract_cpu(dict_features)
    cpu_details = extract_cpu_details(dict_features)
    battery = extract_battery(dict_features)
    charging_type = extract_charging_type(dict_features)
    fast_charging = extract_fast_charging(dict_features)
    screen_size = extract_screen_size(dict_features)
    screen_tech = extract_screen_tech(dict_features)
    screen_resolution = extract_screen_resolution(dict_features)
    screen_type = extract_screen_type(dict_features)
    refresh_rate = extract_refresh_rate(dict_features)
    network = extract_network(dict_features)
    bluetooth = extract_bluetooth(dict_features)
    wifi = extract_wifi(dict_features)
    usb_type_c = extract_usb_type_c(dict_features)
    storage = extract_storage(dict_features)
    upgrade_storage = extract_upgrade_storage(dict_features)
    ram = extract_ram(dict_features)
    sensor = extract_sensor(dict_features)
    sensor_resolution = extract_sensor_resolution(dict_features)
    repairability_index = extract_repairability_index(dict_features)
    warranty = extract_warranty(dict_features)
    made_in = extract_made_in(dict_features)
    brand = extract_brand(dict_features)
    das_head = extract_das_head(dict_features)
    das_chest = extract_das_chest(dict_features)
    das_limbs = extract_das_limb(dict_features)
    height = extract_height(dict_features)
    width = extract_width(dict_features)
    thickness = extract_thickness(dict_features)
    net_weight = extract_net_weight(dict_features)
    price = extract_price(dict_features)
    stars = extract_stars(dict_features)
    reviews = extract_reviews(dict_features)
    image = extract_img(dict_features)
    scraping_time = extract_scraping_time(dict_features)

    return sc.Smartphone(
        model=model,
        color=color,
        os=os,
        sim_type=sim_type,
        sim_number=sim_number,
        cpu=cpu,
        cpu_details=cpu_details,
        battery=battery,
        charging_type=charging_type,
        fast_charging=fast_charging,
        screen_size=screen_size,
        screen_tech=screen_tech,
        screen_resolution=screen_resolution,
        screen_type=screen_type,
        refresh_rate=refresh_rate,
        network=network,
        bluetooth=bluetooth,
        wifi=wifi,
        usb_type_c=usb_type_c,
        storage=storage,
        upgrade_storage=upgrade_storage,
        ram=ram,
        sensor=sensor,
        sensor_resolution=sensor_resolution,
        repairability_index=repairability_index,
        warranty=warranty,
        made_in=made_in,
        brand=brand,
        das_head=das_head,
        das_chest=das_chest,
        das_limbs=das_limbs,
        height=height,
        width=width,
        thickness=thickness,
        net_weight=net_weight,
        price=price,
        stars=stars,
        reviews=reviews,
        image=image,
        scraping_time=scraping_time,
    )
