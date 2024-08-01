from .. import Provider as PersonProvider


class Provider(PersonProvider):
    """
    A Faker provider for generating fake Zulu names in South Africa.
    """

    formats = (
        "{{first_name_male}} {{last_name_male}}",
        "{{first_name_male}} {{last_name_male}}",
        "{{first_name_male}} {{last_name_male}}",
        "{{first_name_male}} {{last_name_male}}",
        "{{first_name_male}} {{last_name_male}} {{last_name_male}}",
        "{{first_name_female}} {{last_name_female}}",
        "{{first_name_female}} {{last_name_female}}",
        "{{first_name_female}} {{last_name_female}}",
        "{{first_name_female}} {{last_name_female}}",
        "{{first_name_female}} {{last_name_female}} {{last_name_female}}",
        "{{prefix_male}} {{first_name_male}} {{last_name_male}}",
        "{{prefix_female}} {{first_name_female}} {{last_name_female}}",
        "{{prefix_male}} {{first_name_male}} {{last_name_male}}",
        "{{prefix_female}} {{first_name_female}} {{last_name_female}}",
    )

    # first names sourced from:
    # 1. https://github.com/faker-js/faker/blob/next/src/locales/yo_NG/person/last_name.ts
    # 2. https://github.com/faker-js/faker/blob/next/src/locales/yo_NG/person/male_first_name.ts

    first_names_male = (
        "Abayomi",
        "Abiodun",
        "Abiona",
        "Adebiyi",
        "Adebowale",
        "Adedayo",
        "Adedeji",
        "Adekitan",
        "Adekola",
        "Adekunle",
        "Adeleke",
        "Adeniyi",
        "Adeolu",
        "Adeoti",
        "Aderopo",
        "Adeshina",
        "Adesoji",
        "Adetayo",
        "Adeyi",
        "Adigun",
        "Afolarin",
        "Ajala",
        "Ajani",
        "Akanmu",
        "Akinkunmi",
        "Akinlabi",
        "Akinwale",
        "Alade",
        "Alamu",
        "Anjolaoluwa",
        "Ayinde",
        "Ayodeji",
        "Ayodele",
        "Babasola",
        "Babatunji",
        "Babawale",
        "Damife",
        "Demilade",
        "Durodola",
        "Ekundayo",
        "Esupofo",
        "Folu",
        "Gbadebo",
        "Gbolahan",
        "Gbowoade",
        "Ibidapo",
        "Ige",
        "Ikeoluwa",
        "Inioluwa",
        "Iseoluwa",
        "Ishola",
        "Juwon",
        "Keji",
        "Kolawole",
        "Korede",
        "Leke",
        "Lere",
        "Niyilolawa",
        "Oba",
        "ObaniJesu",
        "Ogooluwa",
        "Oke",
        "Oladare",
        "Oladimeji",
        "Olakunle",
        "Olanrewaju",
        "Olansile",
        "Olumorotimi",
        "Oluwafemi",
        "Oluwagbemiga",
        "Oluwamumibori",
        "Oluwamuyiwa",
        "Oluwasanmi",
        "Oluwasegun",
        "Oluwole",
        "Omobobola",
        "Omotayo",
        "Osunleke",
        "Seye",
        "Shekoni",
        "Sijuade",
        "Tade",
        "Temidayo",
        "Toki",
        "Tokunbo",
        "Tomori",
    )
    first_names_female = (
        "Aanuoluwapo",
        "Abebi",
        "Abeni",
        "Abosede",
        "Adebukola",
        "Adenike",
        "Adepeju",
        "Adesewa",
        "Adesua",
        "Adetoke",
        "Adetoun",
        "Adunni",
        "Ajoke",
        "Amoke",
        "Amope",
        "Arike",
        "Arinola",
        "Asake",
        "Atinuke",
        "Awero",
        "Ayinke",
        "Ayoka",
        "Bolatito",
        "Boluwatife",
        "Bunmi",
        "Doyinsola",
        "Eniola",
        "Ewatomi",
        "Fadekemi",
        "Faderera",
        "Fehintola",
        "Fibikemi",
        "Fikayomi",
        "Folashade",
        "Ibironke",
        "Iretioluwa",
        "Iyabode",
        "Iyadunni",
        "Kikelomo",
        "Modupe",
        "Mofifoluwa",
        "Mojisola",
        "Mojisoluwa",
        "Moradeke",
        "Morayo",
        "Morenike",
        "Morolake",
        "Mosinmileoluwa",
        "Mosunmola",
        "Motunrayo",
        "Moyosore",
        "Ninioluwa",
        "Olajumoke",
        "Olasunmbo",
        "Ololade",
        "Olufunke",
        "Olufunmilayo",
        "Oluwakemi",
        "Omobolanle",
        "Omodunni",
        "Omolabake",
        "Omolara",
        "Omosalewa",
        "Omotara",
        "Omotola",
        "Omotoun",
        "Omowumi",
        "Oreofe",
        "Oyenike",
        "Oyindasola",
        "Radeke",
        "Ronke",
        "Segilola",
        "Similoluwa",
        "Simisola",
        "Sowande",
        "Subomi",
        "Titilayo",
        "Tolulope",
        "Toluwanimi",
        "Wuraola",
        "Yejide",
        "Yetunde",
        "Yewande",
    )

    first_names = first_names_male + first_names_female

    # last names sourced from :
    # 1. https://github.com/faker-js/faker/blob/next/src/locales/yo_NG/person/last_name.ts
    last_names_male = (
        "Adebisi",
        "Adegbite",
        "Adegoke",
        "Adekunle",
        "Adelakun",
        "Adeleke",
        "Adelusi",
        "Ademiluyi",
        "Aderibigbe",
        "Aderogba",
        "Adesiyan",
        "Adeyemo",
        "Adisa",
        "Afolabi",
        "Afolayan",
        "Afonja",
        "Ajao",
        "Ajayi",
        "Ajewole",
        "Akinrinola",
        "Alabi",
        "Aloba",
        "Awodiran",
        "Awolowo",
        "Ayandokun",
        "Ayoola",
        "Babtunde",
        "Bakare",
        "Balogun",
        "Bamidele",
        "Bamiloye",
        "Edun",
        "Fadipe",
        "Fagunwa",
        "Fajimi",
        "Falabi",
        "Faleti",
        "Faloye",
        "Fasasi",
        "Ibikunle",
        "Ilori",
        "Ilupeju",
        "Iyanda",
        "Jaiyeola",
        "Kolade",
        "Kosoko",
        "Koya",
        "Makinde",
        "Makinwa",
        "Morawo",
        "Ninalowo",
        "Odetola",
        "Odunsi",
        "Ogindan",
        "Oginni",
        "Ogulana",
        "Ogunbamigbe",
        "Ogunbiyi",
        "Ogunbo",
        "Ogunde",
        "Ogunwobi",
        "Ogunyeye",
        "Ojo",
        "Ojua",
        "Olabode",
        "Oladipupo",
        "Olaiya",
        "Olasupo",
        "Olowokeere",
        "Oloyede",
        "Olubode",
        "Olugbayila",
        "Olujimi",
        "Olukotun",
        "Olukunga",
        "Olusanya",
        "Oluwagbemi",
        "Omidina",
        "Omojola",
        "Omotoso",
        "Oparinde",
        "Oshin",
        "Osuntokun",
        "Owokoniran",
        "Owolabi",
        "Owoyemi",
        "Oyadiran",
        "Oyaifo",
        "Oyeniyi",
        "Oyetoro",
        "Oyeyemi",
        "Oyinlola",
        "Paimo",
        "Salako",
        "Salami",
        "Shekoni",
        "Sobowale",
        "Soyinka",
    )

    # last names are not sex dependant
    last_names_female = last_names_male
    last_names = last_names_male + last_names_female

    prefixes_female = (
        "Mrs.",
        "Ms.",
        "Dr.",
        "Alhaja",
        "Mama",
        "Iya",
        "Madam",
        "Chief",
        "Lady",
        "Erelu",
        "Olori",
        "Princess",
    )

    prefixes_male = (
        "Mr.",
        "Dr.",
        "Alhaji",
        "Baba",
        "Ogbeni",
        "Oloye",
        "Chief",
        "Prince",
        "Oba",
        "Kabiyesi",
    )