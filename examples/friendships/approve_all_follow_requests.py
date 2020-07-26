from instauto.api.client import ApiClient
import os

from instauto.api.actions.structs.friendships import ApproveFollowRequest, PendingFollowRequests


if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(user_name="your_username", password="your_password")
        client.login()
        client.save_to_disk('./.instauto.save')

    p = PendingFollowRequests()
    users = client.get_follow_requests(p)

    for user in users:  # approves all requests
        a = ApproveFollowRequest.create(str(user['pk']))
        resp = client.approve_follow_request(a)