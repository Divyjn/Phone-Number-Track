# Phone-Number-Track

This project demonstrates how to locate a phone number geographically and display its location on a map using Python. The application leverages libraries such as `phonenumbers`, `folium`, and the OpenCage Geocoder API.

## Features

- **Phone Number Parsing**: Parse and validate phone numbers, including identifying the country.
- **Geographic Location**: Retrieve the geographical location of the phone number.
- **Carrier Information**: Identify the carrier/service provider for the phone number.
- **Mapping**: Generate an interactive map pinpointing the location of the phone number.

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.x installed on your system.
- An API key from [OpenCage Geocoder](https://opencagedata.com/).
- Required Python libraries installed (see below).

## Installation

1. **Clone the Repository**

```bash
https://github.com/your-username/phone-number-locator.git
cd phone-number-locator
```

2. **Install Dependencies**

Install the required Python libraries using `pip`:

```bash
pip install phonenumbers folium opencage
```

3. **Set Up API Key**

Replace the `Key` variable in the script with your OpenCage Geocoder API key:

```python
Key = "your-api-key-here"
```

## Usage

1. Run the script:

```bash
python locator.py
```

2. Enter the phone number along with the country code (e.g., `+917232069038`).

3. The script will display:
   - The geographical location (e.g., city or region).
   - The latitude and longitude of the location.
   - The service provider name.

4. An interactive map will be generated and saved as `Location.html`. Open this file in your browser to view the location.

## Example Output

```text
Enter the PhoneNumber with the country code: +917232069038
Location: Maharashtra, India
Latitude: 19.7515
Longitude: 75.7139
Service provider: Airtel
```

## File Structure

- `locator.py`: Main script for locating the phone number and generating the map.
- `Location.html`: Generated map file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [phonenumbers library](https://pypi.org/project/phonenumbers/)
- [Folium library](https://python-visualization.github.io/folium/)
- [OpenCage Geocoder API](https://opencagedata.com/)

---

Feel free to contribute to this project by submitting issues or pull requests on GitHub.

