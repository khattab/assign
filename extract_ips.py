from Data import CleanData
from IPAddresses import ExtractIPs  # Extract IPs From Input Data.

file_path = 'kavic.txt'
def get_ip_addresses(file_path):
    input_data = []
    input_data.extend(CleanData(file_path).to_list())
    results = ExtractIPs(input_data).get_ipv4_results()
    return results

f = get_ip_addresses(file_path)
print(f)