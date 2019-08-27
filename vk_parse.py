import vk_requests
import json


def parse_vk_group():

    SERVICE_TOKEN = 'ffb24391ffb24391ffb243911fffda3a77fffb2ffb24391a3eac4ce635b403c6ba08f00'
    group_id = '76592277'
    api = vk_requests.create_api(service_token=SERVICE_TOKEN)
    group = api.groups.getMembers(group_id=group_id, fields=['sex', 'bdate', 'city', 'country', 'photo_max_orig',
                                                                'online', 'online_mobile', 'contacts', 'connections',
                                                                'site', 'education', 'universities', 'schools'])
    return group


def file_writer(group):
    with open('vk_parse.json', 'w') as f:
        json.dump(group, f, sort_keys=True, indent=2)


if __name__ == '__main__':

    file_writer(parse_vk_group())