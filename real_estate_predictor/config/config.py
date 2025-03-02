import numpy as np
from real_estate_predictor.utils.dataset_analysis import *
from real_estate_predictor.utils.feature_engineering import *
import pathlib

#CONFIG files for data pipeline modules

DATACLEANER_FILE = pathlib.Path(__file__).parent.parent.absolute().joinpath('storage', 'processors', 'datacleaner_2025-02-28T19-02-26.pkl')
FEATURE_ENGINEERING_FILE = pathlib.Path(__file__).parent.parent.absolute().joinpath('storage', 'processors', 'featureengineering_2025-02-28T19-02-26.pkl')
PREPROCESSOR_FILE = pathlib.Path(__file__).parent.parent.absolute().joinpath('storage', 'processors', 'processor_2025-02-28T19-02-26.pkl')


#CONFIG file for model path

MODEL_FILE = pathlib.Path(__file__).parent.parent.absolute().joinpath('storage', 'production', 'model.pkl')

#Configuration parameters for generate_dataset

#Global api config for Repliers
# https://api.repliers.io/listings?resultsPerPage=100&type=lease&type=sale&fields=soldDate,address.city,address.area,address.district,address.neighborhood,address.zip,details.numBathrooms,details.numBedrooms,details.style,listPrice,listDate,details.sqft,details.propertyType,details.numParkingSpace,details.numGarageSpaces,details.numKitchens,details.numDrivewaySpaces,details.description,details.numParkingSpaces,details.extras,details.numRooms,condominium.ammenities,condominium.fees,nearby.ammenities,type,class,map,soldPrice&pageNum={i}&minSoldDate={start_date}&maxSoldDate={end_date}&class=condo&class=residential&status=U&lastStatus=Lsd&lastStatus=Sld"
LISTING_PARAMETERS = {
    "resultsPerPage": "100",
    "type": ["lease","sale"],
    "fields" : "soldDate,address.city,address.area,address.district,address.neighborhood"
                ",address.zip,details.numBathrooms,details.numBedrooms,details.style,listPrice,"
                "listDate,details.sqft,details.propertyType,details.numParkingSpace,details.numGarageSpaces,"
                "details.numKitchens,details.numDrivewaySpaces,details.description,details.numParkingSpaces,"
                "details.extras,details.numRooms,condominium.ammenities,condominium.fees,nearby.ammenities,"
                "type,class,map,soldPrice",
    "class" : ["condo","residential"],
    "status": "U",
    "lastStatus": ["Lsd","Sld"]
}

#neighbourhood configuration parameters

#"https://api.repliers.io/listings?type={type}&listings=false&neighborhood={location}&status=U&lastStatus={lastStatus}&statistics=grp-mth,avg-listPrice,avg-soldPrice,cnt-available,cnt-closed,med-daysOnMarket,avg-daysOnMarket,med-soldPrice,med-listPrice&minBeds={bed}&maxBeds={bed}&minSoldDate=2021-01-01&maxSoldDate=2023-12-31&minListDate=2021-01-01&maxListDate=2023-12-31"
NEIGHBOURHOOD_PARAMETERS = {
    "listings": "false",
    "status": "U",
    "statistics": "grp-mth,avg-listPrice,"
                  "avg-soldPrice,cnt-available,cnt-closed,"
                  "med-daysOnMarket,avg-daysOnMarket,med-soldPrice,med-listPrice"
}

NEIGHBOURHOOD_KEYS = ["soldPrice", "listPrice", "available", "daysOnMarket", "closed"]

NEIGHBOURHOOD_TYPES = ["sale","lease"]

NEIGHBOURHOOD_NUMBEDROOMS = [1,2,3,4]

NEIGHBOURHOODS = [
    'Waterfront Communities C1',
    'Church-Yonge Corridor',
    'Bay Street Corridor',
    'City Centre',
    'Willowdale East',
    'Niagara',
    'Mimico',
    'Waterfront Communities C8',
    'Mount Pleasant West',
    'Unionville',
    'Islington-City Centre West',
    'Bayview Village',
    'Annex',
    'Moss Park',
    'Hurontario',
    'Henry Farm',
    'Rural Oakville',
    'Vaughan Corporate Centre',
    'Bowmanville',
    'Northwest Brampton',
    'South Riverdale',
    'Willowdale West',
    'Langstaff',
    'Stoney Creek',
    'Sandringham-Wellington',
    'Central Erin Mills',
    'Concord',
    'Churchill Meadows',
    'Patterson',
    'Central',
    'Bendale',
    'Lakeview',
    'Stouffville',
    'Woburn',
    'Banbury-Don Mills',
    'Agincourt South-Malvern West',
    'Dovercourt-Wallace Emerson-Junction',
    'High Park-Swansea',
    'Erin Mills',
    'Maple',
    "Fletcher's Meadow",
    'Bradford',
    'Georgetown',
    'Downsview-Roding-CFB',
    'Vellore Village',
    'Kensington-Chinatown',
    'Waterdown',
    'East Credit',
    'West Oak Trails',
    'Regent Park',
    'Bram East',
    'Little Portugal',
    'The Beaches',
    'Windfields',
    'Don Valley Village',
    'Orangeville',
    'Alcona',
    'Cornell',
    'Courtice',
    'Cooksville',
    'Meadowvale',
    'Lindsay',
    'Clanton Park',
    'Mount Pleasant East',
    'Malvern',
    'Credit Valley',
    'Wasaga Beach',
    'Rural Caledon',
    'Wismer',
    'Clarkson',
    'Brant',
    'Rosedale-Moore Park',
    'Lansing-Westgate',
    'Newtonbrook West',
    'Orillia',
    "L'Amoreaux",
    'Ancaster',
    'Newtonbrook East',
    'Bronte West',
    'Alliston',
    'Cobourg',
    'Painswick South',
    'Stonegate-Queensway',
    "Tam O'Shanter-Sullivan",
    'Haldimand',
    'Lisgar',
    'Old Oakville',
    'South East',
    'Yonge-Eglinton',
    'Holly',
    'Bram West',
    'Yorkdale-Glen Park',
    'Birchcliffe-Cliffside',
    'Uptown Core',
    'Commerce Valley',
    'Berczy',
    'Collingwood',
    'Monaghan',
    'Yonge-St. Clair',
    'Glen Abbey',
    'Samac',
    'Trinity-Bellwoods',
    'Northcrest',
    'Pringle Creek',
    'Ardagh',
    'Alton',
    'University',
    'Cabbagetown-South St. James Town',
    'Junction Area',
    'Oak Ridges',
    'River Oaks',
    'Keswick South',
    'Appleby',
    'Dorset Park',
    'Rural Innisfil',
    'Wexford-Maryvale',
    'Innis-Shore',
    'SE',
    'Beverley Glen',
    'Crosby',
    'Roncesvalles',
    'Bay Ridges',
    'West Hill',
    'Flemingdon Park',
    'Parkwoods-Donalda',
    'Ford',
    'Bedford Park-Nortown',
    'Jefferson',
    'West Humber-Clairville',
    'Rouge E11',
    'LaSalle',
    'Meadowvale Village',
    'York University Heights',
    'Donevan',
    'North Richvale',
    'Central West',
    'East Woodbridge',
    "O'Neill",
    'Port Credit',
    'Newcastle',
    'Crestwood-Springfarm-Yorkhill',
    'Madoc',
    'Brooklin',
    'Rural Whitby',
    'North St. James Town',
    'High Park North',
    'Beaty',
    'Clairlea-Birchmount',
    'Dempsey',
    'Greensborough',
    'Williamsburg',
    'Holland Landing',
    'East End-Danforth',
    'Leaside',
    'Long Branch',
    'Iroquois Ridge North',
    'Applewood',
    'Northeast Ajax',
    'Eastdale',
    'Clarke',
    'Doncrest',
    'Angus',
    'Erindale',
    'Palmerston-Little Italy',
    'Oakwood Village',
    'Greenwood-Coxwell',
    'Willmott',
    'West Woodbridge',
    'Oak Ridges Lake Wilcox',
    'Mississauga Valleys',
    'Kleinburg',
    'Taunton',
    'Bronte East',
    'Agincourt North',
    'Danforth Village-East York',
    'Queen Street Corridor',
    'South Parkdale',
    'Thornhill',
    'Brampton North',
    'Rural Smith-Ennismore-Lakefield',
    'Palermo West',
    'McLaughlin',
    'Lawrence Park South',
    'Forest Hill South',
    'Northwest Ajax',
    'Rathwood',
    'St. Andrew-Windfields',
    'Bristol-London',
    'Rural Pickering',
    'Steeles',
    'Orchard',
    'Rolling Acres',
    'Lawrence Park North',
    'Casa Loma',
    'Malton',
    'Central Park',
    'Aurora Highlands',
    'Paris',
    'Woodland Hill',
    'Grange Hill East',
    'Westbrook',
    'Otonabee',
    'Englemount-Lawrence',
    'Rouge Woods',
    'Central Newmarket',
    'South Richvale',
    'Hillcrest Village',
    'Keswick North',
    'Milliken',
    'Centennial',
    'Edenbridge-Humber Valley',
    'Stoney Creek Mountain',
    'SW',
    'Stonehaven-Wyndham',
    "Fletcher's Creek South",
    'Rockcliffe-Smythe',
    'Harrison',
    'Port Hope',
    'Weston-Pellam Park',
    'Blue Grass Meadows',
    'Milliken Mills East',
    'Sharon',
    'Northgate',
    'Downtown Brampton',
    'Bathurst Manor',
    'Summerhill Estates',
    'Humewood-Cedarvale',
    'Ashburnham',
    'Crown Point',
    'Westminster-Branson',
    'Cliffcrest',
    'Downtown',
    'Middlefield',
    'Etobicoke West Mall',
    'Rural Vaughan',
    'Harding',
    'Vanier',
    'Eglinton East',
    'Eringate-Centennial-West Deane',
    'Streetsville',
    'Pleasant View',
    'Brampton West',
    'Brownridge',
    'Lynde Creek',
    'Pinecrest',
    'Rural Aurora',
    'College Park',
    'Downtown Whitby',
    'Observatory',
    "O'Connor-Parkview",
    'Briar Hill-Belgravia',
    'Shelburne',
    'Brampton East',
    'East York',
    'Liverpool',
    'North I',
    'Mill Pond',
    'Rural Galway-Cavendish and Harvey',
    'Uxbridge',
    'Midland',
    'Rural Richmond Hill',
    'Duffin Heights',
    'East I',
    'Alderwood',
    'Fergus',
    'Heart Lake West',
    'Roseland',
    'Dundas',
    'Binbrook',
    'Mineola',
    'Scott',
    'Mount Olive-Silverstone-Jamestown',
    'Weston',
    'Gorham-College Manor',
    'South X',
    'Aileen-Willowbrook',
    'Eastlake',
    'Cedarwood',
    'Brookhaven-Amesbury',
    'Brighton',
    'Kingsview Village-The Westway',
    'North S',
    'Headon',
    'Aurora Village',
    'Willowridge-Martingrove-Richview',
    'Port Perry',
    'Port Whitby',
    'Aurora Heights',
    "Sutton & Jackson's Point",
    'Central East',
    'New Toronto',
    'Southgate',
    'Woodbine Corridor',
    'Wychwood',
    'Corso Italia-Davenport',
    'Tottenham',
    'Bayview Wellington',
    "Fletcher's West",
    'Rose',
    'Dufferin Grove',
    'South West',
    'South V',
    'Scarborough Village',
    'Bridle Path-Sunnybrook-York Mills',
    'Runnymede-Bloor West Village',
    'Shoreacres',
    'Morningside',
    'Huron Heights-Leslie Valley',
    'Kennedy Park',
    'Bayview Northeast',
    'Rural Tiny',
    'Pine Ridge',
    'Glenfield-Jane Heights',
    'Sheridan',
    'North Riverdale',
    'Keelesdale-Eglinton West',
    'Victoria Village',
    'Beasley',
    'Lorne Park',
    'Town Centre',
    'Sonoma Heights',
    'Brant Hills',
    'Creditview',
    'Cobban',
    'Thorncliffe Park',
    'Amberlea',
    'East G',
    'North R',
    'Royal Orchard',
    'North C',
    'Coates',
    'North M',
    'NW',
    'Brampton South',
    'NE',
    'Devonsleigh',
    'Woodbine-Lumsden',
    'Northwood Park',
    'Northwest Sandalwood Parkway',
    'Markham Village',
    'Westgate',
    'Norfolk',
    'Markland Wood',
    'South B',
    'Mount Hope',
    'Guildwood',
    'Queensville',
    'Tansley',
    'Acton',
    'Taunton North',
    'Fenelon Falls',
    'Beaverton',
    'Box Grove',
    'Centennial Scarborough',
    'East H',
    'Painswick North',
    'East C',
    'Fairview',
    'Danforth',
    'East F',
    'Dundalk',
    'Campbellford',
    'Gibson',
    'Bolton East',
    'West Shore',
    'Angus Glen',
    'Snelgrove',
    'Kingsway South',
    'North B',
    'Bobcaygeon',
    'Mountainside',
    'Grandview',
    'Heart Lake East',
    'Avondale',
    'Bayview Woods-Steeles',
    'East D',
    'Village Green-South Unionville',
    'South U',
    'Ottawa',
    'Vaughan Grove',
    'Rural Otonabee-South Monaghan',
    'Rouge E10',
    'Rural Clarington',
    'North F',
    'Letitia Heights',
    'King City',
    'Iroquois Ridge South',
    'Rural Whitchurch-Stouffville',
    'Rural Trent Hills',
    'Caledonia-Fairbank',
    'Old Milton',
    'Highland Creek',
    'Ainslie Wood',
    'Kortright Hills',
    'West Willow Woods',
    'Rural Douro-Dummer',
    'South F',
    'Grove East',
    'Vales of Castlemore',
    'South W',
    'Glenway Estates',
    'Blue Mountain Resort Area',
    'Rural Cavan Monaghan',
    'Mt Albert',
    'South K',
    'Humber Heights',
    'Rural Oro-Medonte',
    'Lakeshore',
    'Princess-Rosethorn',
    'South Y',
    'Islington Woods',
    'East A',
    'Victoria Square',
    "Fletcher's Creek Village",
    'Crescent Town',
    'Vincent',
    'Rural Mono',
    'Rural Scugog',
    'Sandringham-Wellington North',
    'North G',
    'Black Creek',
    'Sunnidale',
    'Rural Barrie Southeast',
    'Guelph South',
    'Rural North Kawartha',
    'Bolton West',
    'Markville',
    'Brock Ridge',
    'Georgian Drive',
    'Rural Uxbridge',
    'Humbermede',
    'Kirkendall',
    'Bayview Hill',
    'Cathedraltown',
    'Village East',
    'South T',
    'Uptown',
    'Broadview North',
    'Walker',
    'Durand',
    'Elora/Salem',
    'East B',
    'Nobleton',
    'Palmer',
    'Timberlea',
    'East K',
    'Humber Summit',
    'Raymerville',
    'Humberlea-Pelmo Park W5',
    'Penetanguishene',
    'Dunnville',
    'Simcoe',
    'South O',
    'North P',
    'Rural Havelock-Belmont-Methuen',
    'Caledon East',
    'Milliken Mills West',
    'Lefroy',
    'Blake-Jones',
    'Mount Dennis',
    'South E',
    'North N',
    'Brechin',
    'Ionview',
    'Rustic',
    'Clearview',
    'Forest Hill North',
    'East M',
    'AY',
    'Elms-Old Rexdale',
    'Two Rivers',
    'Allandale',
    'Wellington',
    'Brantford Twp',
    'Hannon',
    'Homeside',
    'Oakridge',
    'Bullock',
    'Waverley',
    'Cachet',
    'Cundles East',
    'Playter Estates-Danforth',
    'Maple Leaf',
    'Rural Ramara',
    'Rural Severn',
    'North E',
    'Little Lake',
    'Rockwood',
    'Landsdale',
    'Freeman',
    'Goreway Drive Corridor',
    'Rexdale-Kipling',
    'Millbrook',
    'Rural Hamilton',
    'Historic Lakeshore Communities',
    'Colborne',
    'Clairfields',
    'Bolton North',
    'Sarnia',
    'South D'
]

LISTING_HIERARCHY = {
    "class": None,
    "type": None,
    "listPrice": None,
    "listDate": None,
    "soldPrice": None,
    "soldDate": None,
    "address": {
        "area": None,
        "city": None,
        "district": None,
        "neighborhood": None,
        "zip": None
    },
    "details": {
        "numBathrooms": None,
        "numBedrooms": None,
        "style": None,
        "numKitchens": None,
        "numRooms": None,
        "numParkingSpaces": None,
        "sqft": None,
        "propertyType": None,
        "numGarageSpaces": None,
        "numDrivewaySpaces": None,
        "description": None,
        "extras": None,
        "numParkingSpaces": None
    },
    "condominium": {
        "ammenities": None,
        "fees": None
    },
    "nearby": {
        "ammenities": None
    },
    "map": {
        "latitude": None,
        "longitude": None,
    },
}

#Configuration parameters for manipulate_dataset

LISTING_EXPECTED_COLUMNS = ['class', 'type', 'listPrice', 'listDate', 'soldPrice', 'soldDate',
    'city', 'area', 'district', 'neighborhood', 'zip', 'latitude',
    'longitude', 'fees', 'condo_ammenities', 'ammenities', 'numBathrooms',
    'numBedrooms', 'style', 'numKitchens', 'numRooms', 'numParkingSpaces',
    'sqft', 'description', 'extras', 'propertyType', 'numGarageSpaces',
    'numDrivewaySpaces']

LISTING_COLUMN_TO_DTYPE_MAPPING = {
    "class": str,
    "type": str,
    "listPrice": float,
    "listDate": np.datetime64,
    "soldPrice": float,
    "soldDate": np.datetime64,
    "city": str,
    "area": str,
    "district": str,
    "neighborhood": str,
    "zip": str,
    "latitude": float,
    "longitude": float,
    "fees": dict,
    "condo_ammenities": list,
    "ammenities": list,
    "numBathrooms": int, #float,
    "numBedrooms": int, #float,
    "style": str,
    "numKitchens": int, #float,
    "numRooms": int, #float,
    "numParkingSpaces": int, #float,
    "sqft": str,
    "description": str,
    "extras": str,
    "propertyType": str,
    "numGarageSpaces": int, #float,
    "numDrivewaySpaces": int, #float,
}

##

#Configuration parameters for Processor

## Each key in the dictionary is a column name and the value is a list of functions to apply to the column

## col : [func1, func2, func3]

PREPROCESSING_PARAMETERS = {
    "ammenities": [standardize_ammenities_text],
    "condo_ammenities": [standardize_ammenities_text],
    "zip": [standardize_postal_code],
    "area": [standardize_locations_text],
    "district": [standardize_locations_text],
    "neighborhood": [standardize_locations_text],
    "city": [standardize_locations_text],
    "style": [standardize_style_text],
    "propertyType": [standardize_propertyType_text],
}

#Configuration parameters for FeatureEngineering

## Each key in the dictionary is a new feature name and the value is a tuple containing a pre-requisite set of features that need to be in the column to generate the new feature, along with that function name

## new_feature_col : ([col1, col2, col3], feature_engineering_func)

#for now, please add the columns you want IN THE ORDER of the FEATURE_ENGINEERING_PARAMETERS keys
#i.e if you want to add the column "ppsqft", you need to add "sqft_avg" in the create_features function first to avoid errors
FEATURE_ENGINEERING_PARAMETERS = {
    "sqft_avg": (["sqft"], create_sqft_avg_column),
    "ppsqft": (["listPrice", "sqft_avg"], create_ppsqft_column),
    "bedbathRatio": (["numBedrooms", "numBathrooms"], create_bedbathRatio_column),
    "numAmmenities": (["ammenities"], create_num_ammenities_column),
    "has_ammenities_flags": (["ammenities"], create_ammenities_flag_columns),
    "numCondoAmmenities": (["condo_ammenities"], create_num_ammenities_column),
    "postal_code_split_2": (["zip"], create_split_postalcode_column),
    "postal_code_split_3": (["zip"], create_split_postalcode_column),
    "daysOnMarket": (["listDate", "soldDate"], create_dom_column), 
    "previous_months_ppsqft": (
        [
            'avg_soldPrice_currentL1M',
            'med_soldPrice_currentL1M',
            'avg_listPrice_currentL1M',
            'med_listPrice_currentL1M',
            'avg_soldPrice_currentL3M',
            'med_soldPrice_currentL3M',
            'avg_listPrice_currentL3M',
            'med_listPrice_currentL3M',
            'avg_soldPrice_currentL6M',
            'avg_soldPrice_currentL6M',
            'avg_listPrice_currentL6M',
            'avg_listPrice_currentL6M',
            'sqft_avg'
        ],
        create_previous_month_ppsqft_columns
    ),
    "difference_bymonth_columns": (
        [
            'avg_soldPrice_currentL1M',
            'avg_soldPrice_currentL3M',
            'avg_listPrice_currentL1M',
            'avg_listPrice_currentL3M',
            'med_soldPrice_currentL1M',
            'med_soldPrice_currentL3M',
            'med_listPrice_currentL1M',
            'med_listPrice_currentL3M',
            'count_soldPrice_currentL1M',
            'count_soldPrice_currentL3M',
            'count_listPrice_currentL1M',
            'count_listPrice_currentL3M',
            'avg_soldPrice_currentL6M',
            'avg_listPrice_currentL6M',
            'med_soldPrice_currentL6M',
            'med_listPrice_currentL6M',
            'count_soldPrice_currentL6M',
            'count_listPrice_currentL6M',
        ],
        create_difference_bymonth_columns
    ),
    "ratio_bymonth_columns": (
        [
            'avg_soldPrice_currentL1M',
            'avg_soldPrice_currentL3M',
            'avg_listPrice_currentL1M',
            'avg_listPrice_currentL3M',
            'med_soldPrice_currentL1M',
            'med_soldPrice_currentL3M',
            'med_listPrice_currentL1M',
            'med_listPrice_currentL3M',
            'count_soldPrice_currentL1M',
            'count_soldPrice_currentL3M',
            'count_listPrice_currentL1M',
            'count_listPrice_currentL3M',
            'avg_soldPrice_currentL6M',
            'avg_listPrice_currentL6M',
            'med_soldPrice_currentL6M',
            'med_listPrice_currentL6M',
            'count_soldPrice_currentL6M',
            'count_listPrice_currentL6M',
        ],
        create_ratio_bymonth_columns
    ),
}



FEATURE_ENGINEERING_PARAMETERS_old = {
    "sqft" : ([], None),
    "sqft_avg": (["sqft"], create_sqft_avg_column),
    "ppsqft": (["listPrice", "sqft_avg"], create_ppsqft_column),
    "bedbathRatio": (["numBedrooms", "numBathrooms"], create_bedbathRatio_column),
    "has_ammenities_flags": (["ammenities"], create_ammenities_flag_columns),
    #"has_condo_ammenities_flags": (["condo_ammenities"], create_ammenities_flag_columns),
    "numAmmenities": (["ammenities"], create_num_ammenities_column),
    "numCondoAmmenities": (["condo_ammenities"], create_num_ammenities_column),
    "postal_code_split_2": (["zip"], create_split_postalcode_column),
    "postal_code_split_3": (["zip"], create_split_postalcode_column),
    "daysOnMarket": (["listDate", "soldDate"], create_dom_column),
    # "neighborhood_key": (["numbedRoom", "type", "neighborhood", "listDate"], helper_construct_neighbourhood_key_column),
    # "avg_soldPrice_currentL1M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_soldPrice_currentL1M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_soldPrice_currentL1M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_listPrice_currentL1M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_listPrice_currentL1M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_listPrice_currentL1M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_available_currentL1M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_daysOnMarket_currentL1M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_daysOnMarket_currentL1M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_daysOnMarket_currentL1M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_soldPrice_currentL3M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_soldPrice_currentL3M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_soldPrice_currentL3M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_listPrice_currentL3M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_listPrice_currentL3M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_listPrice_currentL3M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_available_currentL3M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_daysOnMarket_currentL3M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_daysOnMarket_currentL3M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_daysOnMarket_currentL3M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_soldPrice_currentL6M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_soldPrice_currentL6M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_soldPrice_currentL6M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_listPrice_currentL6M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_listPrice_currentL6M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_listPrice_currentL6M"    : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_available_currentL6M"  : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "avg_daysOnMarket_currentL6M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "count_daysOnMarket_currentL6M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    # "med_daysOnMarket_currentL6M" : (["neighborhood_key"], merge_neighborhood_previous_columns),
    "avg_soldPrice_ppsqft_currentL1M": (["avg_soldPrice_currentL1M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "med_soldPrice_ppsqft_currentL1M": (["med_soldPrice_currentL1M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "avg_listPrice_ppsqft_currentL1M": (["avg_listPrice_currentL1M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "med_listPrice_ppsqft_currentL1M": (["med_listPrice_currentL1M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "avg_soldPrice_ppsqft_currentL3M": (["avg_soldPrice_currentL3M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "med_soldPrice_ppsqft_currentL3M": (["med_soldPrice_currentL3M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "avg_listPrice_ppsqft_currentL3M": (["avg_listPrice_currentL3M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "med_listPrice_ppsqft_currentL3M": (["med_listPrice_currentL3M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "avg_soldPrice_ppsqft_currentL6M": (["avg_soldPrice_currentL6M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "med_soldPrice_ppsqft_currentL6M": (["avg_soldPrice_currentL6M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "avg_listPrice_ppsqft_currentL6M": (["avg_listPrice_currentL6M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "med_listPrice_ppsqft_currentL6M": (["avg_listPrice_currentL6M", "sqft_avg"], create_previous_month_ppsqft_columns),
    "avg_soldPrice_difference_1M_3M": (["avg_soldPrice_currentL1M", "avg_soldPrice_currentL3M"], create_difference_bymonth_columns),
    "avg_soldPrice_difference_3M_6M": (["avg_soldPrice_currentL3M", "avg_soldPrice_currentL6M"], create_difference_bymonth_columns),
    "avg_listPrice_difference_1M_3M": (["avg_listPrice_currentL1M", "avg_listPrice_currentL3M"], create_difference_bymonth_columns),
    "avg_listPrice_difference_3M_6M": (["avg_listPrice_currentL3M", "avg_listPrice_currentL6M"], create_difference_bymonth_columns),
    "med_soldPrice_difference_1M_3M": (["med_soldPrice_currentL1M", "med_soldPrice_currentL3M"], create_difference_bymonth_columns),
    "med_soldPrice_difference_3M_6M": (["med_soldPrice_currentL3M", "med_soldPrice_currentL6M"], create_difference_bymonth_columns),
    "med_listPrice_difference_1M_3M": (["med_listPrice_currentL1M", "med_listPrice_currentL3M"], create_difference_bymonth_columns),
    "med_listPrice_difference_3M_6M": (["med_listPrice_currentL3M", "med_listPrice_currentL6M"], create_difference_bymonth_columns),
    "count_soldPrice_difference_1M_3M": (["count_soldPrice_currentL1M", "count_soldPrice_currentL3M"], create_difference_bymonth_columns),
    "count_soldPrice_difference_3M_6M": (["count_soldPrice_currentL3M", "count_soldPrice_currentL6M"], create_difference_bymonth_columns),
    "count_listPrice_difference_1M_3M": (["count_listPrice_currentL1M", "count_listPrice_currentL3M"], create_difference_bymonth_columns),
    "count_listPrice_difference_3M_6M": (["count_listPrice_currentL3M", "count_listPrice_currentL6M"], create_difference_bymonth_columns),
    "avg_soldPrice_ratio_1M_3M": (["avg_soldPrice_currentL1M"], create_ratio_bymonth_columns),
    "avg_soldPrice_ratio_3M_6M": (["avg_soldPrice_currentL3M"], create_ratio_bymonth_columns),
    "avg_listPrice_ratio_1M_3M": (["avg_listPrice_currentL1M"], create_ratio_bymonth_columns),
    "avg_listPrice_ratio_3M_6M": (["avg_listPrice_currentL3M"], create_ratio_bymonth_columns),
    "med_soldPrice_ratio_1M_3M": (["med_soldPrice_currentL1M"], create_ratio_bymonth_columns),
    "med_soldPrice_ratio_3M_6M": (["med_soldPrice_currentL3M"], create_ratio_bymonth_columns),
    "med_listPrice_ratio_1M_3M": (["med_listPrice_currentL1M"], create_ratio_bymonth_columns),
    "med_listPrice_ratio_3M_6M": (["med_listPrice_currentL3M"], create_ratio_bymonth_columns),
    "count_soldPrice_ratio_1M_3M": (["count_soldPrice_currentL1M"], create_ratio_bymonth_columns),
    "count_soldPrice_ratio_3M_6M": (["count_soldPrice_currentL3M"], create_ratio_bymonth_columns),
    "count_listPrice_ratio_1M_3M": (["count_listPrice_currentL1M"], create_ratio_bymonth_columns),
    "count_listPrice_ratio_3M_6M": (["count_listPrice_currentL3M"], create_ratio_bymonth_columns),
} 

FEATURE_ENGINEERING_COLUMNS = {
    #mapping is pre_req column : [function_for_new_column, {new_col_name: existence_of_col_as_pre_req}]
    "sqft" : ([create_sqft_avg_column], {"sqft_avg": True}),
    "sqft_avg": (create_ppsqft_column, {"ppsqft": False}),
    "ppsqft": (["listPrice", "sqft_avg"], create_ppsqft_column),
    "bedbathRatio": (["numBedrooms", "numBathrooms"], create_bedbathRatio_column),
    "has_ammenities_flags": (["ammenities"], create_ammenities_flag_columns),
    "has_condo_ammenities_flags": (["condo_ammenities"], create_ammenities_flag_columns),
    "numAmmenities": (["ammenities"], create_num_ammenities_column),
    "numCondoAmmenities": (["condo_ammenities"], create_num_ammenities_column),
    "postal_code_split_2": (["zip"], create_split_postalcode_column),
    "postal_code_split_3": (["zip"], create_split_postalcode_column),
    "daysOnMarket": (["listDate", "soldDate"], create_dom_column),
    }

TEST_FEATURE_ENGINEERING_PARAMETERS_1= {
    "listPrice": ([], None),
    "sqft" : ([], None),
    "ppsqft": (["listPrice", "sqft_avg"], create_ppsqft_column),
    "sqft_avg": (["sqft"], create_sqft_avg_column),
}

TEST_FEATURE_ENGINEERING_PARAMETERS_2= {
    "sqft" : ([], None),
    "ppsqft": (["listPrice", "sqft_avg"], create_ppsqft_column),
    "sqft_avg": (["sqft"], create_sqft_avg_column),
}

## Configuration Parameters for Pipeline

CONFIGURATION_PARAMETERS = {
    
}