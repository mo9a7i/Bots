# GitHub Bot 3.0
# Getting ready for prediction model by gathering data on the users
import os,requests,time,datetime,json,random,sys
from dotenv import load_dotenv

class GithubBot:
    def __init__(self):
        print("Initializing GitHub Bot...")
        # Check if .env file exists
        if not os.path.exists('.env'):
            print("ERROR: .env file not found!")
            print("Please create .env file with:")
            print("token=your_github_token")
            print("my_username=your_github_username")
            sys.exit(1)
            
        # Load environment variables
        load_dotenv()
        self.token = os.environ.get('token')
        self.my_username = os.environ.get('my_username')
        
        if not self.token or not self.my_username:
            print("ERROR: Missing environment variables!")
            print(f"token: {'✓' if self.token else '✗'}")
            print(f"my_username: {'✓' if self.my_username else '✗'}")
            sys.exit(1)
            
        print(f"Authenticated as: {self.my_username}")
        self.special = []
        self.target_users = []
        self.headers = {"Authorization": f"Bearer {self.token}","X-GitHub-Api-Version": "2022-11-28"}
        self.blacklist = {}
        print("Loading configurations...")
        self.load_config()
        self.check_blacklist()
        print("Fetching current followers and following...")
        self.followers = []
        self.following = []
        self.find_followers()
        self.find_following()
        print("Starting automation...")
        self.automate()

    def load_config(self):
        """Load special users and target users from config files"""
        print("Loading special users...")
        try:
            with open('config/special_users.json', 'r') as f:
                self.special = json.load(f)['special_users']
            print(f"Loaded {len(self.special)} special users")
        except FileNotFoundError:
            print("WARNING: special_users.json not found, creating empty file")
            with open('config/special_users.json', 'w') as f:
                json.dump({"special_users": []}, f, indent=4)

        print("Loading target users...")
        try:
            with open('config/target_users.json', 'r') as f:
                self.target_users = json.load(f)['target_users']
            print(f"Loaded {len(self.target_users)} target users")
        except FileNotFoundError:
            print("WARNING: target_users.json not found, creating empty file")
            with open('config/target_users.json', 'w') as f:
                json.dump({"target_users": []}, f, indent=4)

    # I created a blacklist and these users will not be followed again
    def check_blacklist(self):
        try:
            with open('blacklist.json','r') as f:
                self.blacklist:dict = json.load(f)
        except FileNotFoundError:
            pass

    # This method finds all the followers that i follow
    def find_followers(self):
        print(f"\n🔍 Fetching followers list for {self.my_username}")
        url = f'https://api.github.com/users/{self.my_username}/followers'
        page = 1

        self.followers = []
        loop = True
        while loop:
            furl = f"{url}?page={page}&per_page=100"
            print(f"\n📄 Fetching followers page {page} (100 users per page)")
            response = requests.get(furl,headers=self.headers)

            if response.status_code == 200:
                if response.json() == []:
                    loop = False
                else:
                    print(f"✅ Status {response.status_code}: Found {len(response.json())} followers on page {page}")
                    for item in response.json():
                        self.followers.append(item['login'])
                        print(f"  → User: {item['login']} (Follower #{len(self.followers)})")
                    page += 1
            else:
                print(f"❌ ERROR: API returned status {response.status_code}")
                print(f"📝 Response: {response.json()}")
                print('Time to give a break')
                for i in range(5):
                    print(f"{i} seconds, {5-i} seconds left to restart")
                    time.sleep(1)
        print(f"\n✨ Complete! Found {len(self.followers)} total followers\n")

    # This method finds all the people I follow
    def find_following(self):
        print(f"\n�� Fetching following list for {self.my_username}")
        url = f'https://api.github.com/users/{self.my_username}/following'
        page = 1

        self.following = []
        loop = True
        while loop:
            furl = f"{url}?page={page}&per_page=100"
            print(f"\n📄 Fetching following page {page} (100 users per page)")
            response = requests.get(furl,headers=self.headers)

            if response.status_code == 200:
                if response.json() == []:
                    loop = False
                else:
                    print(f"✅ Status {response.status_code}: Found {len(response.json())} users you follow on page {page}")
                    for item in response.json():
                        self.following.append(item['login'])
                        print(f"  → User: {item['login']} (Following #{len(self.following)})")
                    page += 1
            else:
                print(f"❌ ERROR: API returned status {response.status_code}")
                print(f"📝 Response: {response.json()}")
                print('Time to give a break')
                for i in range(5):
                    print(f"{i} seconds, {5-i} seconds left to restart")
                    time.sleep(1)
        print(f"\n✨ Complete! Found {len(self.following)} total users you follow\n")

    # The following method follows one specific GitHub account
    def follow_one_account(self,account:str):
        url = f"https://api.github.com/user/following/{account}"
        response = requests.put(url, headers=self.headers)
        if response.status_code == 204:
            if self.check_your_following(account):
                day = datetime.datetime.now().day
                month = datetime.datetime.now().month
                year = datetime.datetime.now().year
                date_string = f"{day}-{month}-{year}"
                try:
                    with open('config/following.json','r') as f:
                        following = json.load(f)
                        following[account] = {
                            "date": date_string,
                            "followed_by_bot": True,
                            "followed_back": False
                        }
                    with open('config/following.json', 'w') as f:
                        json.dump(following,f,indent=4)
                except FileNotFoundError:
                    with open('config/following.json','w') as f:
                        following = {}
                        following[account] = {
                            "date": date_string,
                            "followed_by_bot": True,
                            "followed_back": False
                        }
                    with open('config/following.json', 'w') as f:
                        json.dump(following, f, indent=4)
                print(f"Successfully followed {account}!")
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5-i} seconds to restart")
                time.sleep(1)
            self.follow_one_account(account)

    # The following method checks if they are following you or not
    def check_following(self,account:str)->bool:
        url = f"https://api.github.com/users/{account}/following/{self.my_username}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 204:
            # Update followed_back status in following.json
            try:
                with open('config/following.json', 'r') as f:
                    following = json.load(f)
                    if account in following:
                        following[account]["followed_back"] = True
                        with open('config/following.json', 'w') as f:
                            json.dump(following, f, indent=4)
            except FileNotFoundError:
                pass
            return True
        elif response.status_code == 404:
            return False
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.check_following(account)

    # This method checks if you are actually following the account
    # I added this method because there are accounts that the API says that you followed but in reality you did not end up following them
    def check_your_following(self,account:str)->bool:
        url = f"https://api.github.com/users/{self.my_username}/following/{account}"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 204:
            return True
        elif response.status_code == 404:
            return False
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.check_following(account)


    # The following method unfollows one specific GitHub account
    def unfollow_one_account(self,account:str):
        url = f"https://api.github.com/user/following/{account}"

        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            with open('config/following.json','r') as f:
                following:dict = json.load(f)
            date:str = following[account].split("-")
            following.pop(account)
            with open('config/following.json','w') as f:
                json.dump(following,f,indent=4)

            today = datetime.datetime.now()
            d1_day = int(date[0])
            d1_month = int(date[1])
            d1_year = int(date[2])
            d1 = datetime.datetime(day=d1_day,month=d1_month,year=d1_year)
            d2 = datetime.datetime.now()
            days = (d2-d1).days
            data_dictionary = self.gather_account_data(account)

            if self.check_following(account):
                data_dictionary['result'] = True
                data_dictionary['days_to_follow'] = days
            else:
                data_dictionary['result'] = True
                data_dictionary['days_to_follow'] = -1

            try:
                with open('results.json','r') as f:
                    dictionary = json.load(f)
                with open('results.json','w') as f:
                    dictionary[account] = data_dictionary
                    json.dump(dictionary,f,indent=4)
            except FileNotFoundError:
                with open('results.json','w') as f:
                    json.dump({account:data_dictionary},f,indent=4)

            print(f"Successfully unfollowed {account}!")
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.unfollow_one_account(account)

    # This method unfollows accounts that have followed us back or accounts that have not followed us back for 7 days and puts them in a blacklist
    def unfollow_accounts(self):
        self.find_followers()
        with open('config/following.json','r') as f:
            following:dict = json.load(f)

        for account in following:
            if account not in self.special:
                if account in self.followers:
                    time.sleep(1)
                    self.unfollow_one_account(account)
                else:
                    date_string = following[account]["date"].split("-")
                    d1_day = int(date_string[0])
                    d1_month = int(date_string[1])
                    d1_year = int(date_string[2])
                    d1 = datetime.datetime(day=d1_day,month=d1_month,year=d1_year)
                    d2 = datetime.datetime.now()
                    days = (d2-d1).days
                    if days >= 7:
                        time.sleep(1)
                        self.unfollow_one_account(account)
                        d2_day = d2.day
                        d2_month = d2.month
                        d2_year = d2.year
                        today_string = f"{d2_day}-{d2_month}-{d2_year}"
                        try:
                            with open('config/blacklist.json','r') as f:
                                blacklist = json.load(f)
                                blacklist[account] = today_string
                            with open('config/blacklist.json','w') as f:
                                json.dump(blacklist,f,indent=4)
                        except FileNotFoundError:
                            with open('blacklist.json','w') as f:
                                json.dump({account:today_string},f,indent=4)

    # Gathers data on the user
    def gather_account_data(self,account:str) -> dict:
        url = f"https://api.github.com/users/{account}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            dictionary = {}
            dictionary['name'] = account
            dictionary['creation_date'] = data['created_at'].split("T")[0]
            dictionary['update_date'] = data['updated_at'].split("T")[0]
            dictionary['followers'] = data['followers']
            dictionary['following'] = data['following']
            ratio = None
            if data['following'] == 0:
                ratio = data['followers']/1
            else:
                ratio = data['followers']/data['following']
            dictionary['ratio'] = ratio
            dictionary['repo_count'] = data['public_repos']

            if data['twitter_username'] is None:
                dictionary['twitter'] = False
            else:
                dictionary['twitter'] = True

            if data['bio'] is None:
                dictionary['bio'] = False
            else:
                dictionary['bio'] = True

            if data['email'] is None:
                dictionary['email'] = False
            else:
                dictionary['email'] = True

            if data['location'] is None:
                dictionary['location'] = False
            else:
                dictionary['location'] = True
            print(dictionary)
            return dictionary
        else:
            time.sleep(5)
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.gather_account_data(account)

    # The following method follows accounts
    def follow_accounts(self):
        if not self.target_users:
            print("❌ Error: No target users found in config/target_users.json")
            return
        
        # Load or create scanned targets file
        try:
            with open('config/scanned_targets.json', 'r') as f:
                scanned_targets = json.load(f)
        except FileNotFoundError:
            scanned_targets = {}
        
        # Filter out recently scanned targets
        current_month = datetime.datetime.now().strftime("%Y-%m")
        available_targets = []
        for target in self.target_users:
            last_scan = scanned_targets.get(target, {}).get('last_scan', '')
            if not last_scan.startswith(current_month):
                available_targets.append(target)
        
        if not available_targets:
            print("❌ All target users have been scanned this month!")
            return
        
        account_chosen = random.choice(available_targets)
        print(f"\n🎯 Selected target user to analyze: {account_chosen}")
        accounts = []
        url = f'https://api.github.com/users/{account_chosen}/followers'
        page = 1

        loop = True
        while loop:
            furl = f"{url}?page={page}&per_page=100"
            print(f"\n📄 Fetching followers of {account_chosen} - Page {page}")
            response = requests.get(furl, headers=self.headers)

            if response.status_code == 200:
                if response.json() == []:
                    loop = False
                else:
                    print(f"✅ Status {response.status_code}: Processing followers")
                    for item in response.json():
                        accounts.append(item['login'])
                        print(f"  → Found user: {item['login']} (#{len(accounts)} from {account_chosen}'s followers)")
                    page += 1
            else:
                print(f"❌ API Error {response.status_code}: {response.json()}")
                print('Time to give a break')
                for i in range(5):
                    print(f"{i} seconds, {5-i} seconds left to restart")
                    time.sleep(1)

        # Update scanned targets file
        scanned_targets[account_chosen] = {
            'last_scan': datetime.datetime.now().strftime("%Y-%m-%d"),
            'followers_found': len(accounts),
            'successful_follows': 0,
            'skipped_users': {
                'blacklisted': 0,
                'special': 0,
                'already_following': 0,
                'already_follower': 0
            }
        }
        with open('config/scanned_targets.json', 'w') as f:
            json.dump(scanned_targets, f, indent=4)

        count = 0
        print(f"\n👥 Processing {len(accounts)} potential users to follow")
        for account in accounts:
            if account not in self.blacklist:
                scanned_targets[account_chosen]['skipped_users']['blacklisted'] += 1
                if account not in self.special:
                    scanned_targets[account_chosen]['skipped_users']['special'] += 1
                    if account not in self.following:
                        scanned_targets[account_chosen]['skipped_users']['already_following'] += 1
                        if account not in self.followers:
                            scanned_targets[account_chosen]['skipped_users']['already_follower'] += 1
                            if count != 500:
                                time.sleep(1)
                                print(f"\n🤝 Attempting to follow: {account}")
                                print(f"  → Found via: {account_chosen}'s followers")
                                print(f"  → Follow count today: {count}/500")
                                self.follow_one_account(account)
                                if self.check_your_following(account):
                                    count += 1
                                    scanned_targets[account_chosen]['successful_follows'] += 1
                                    with open('config/scanned_targets.json', 'w') as f:
                                        json.dump(scanned_targets, f, indent=4)


    # This method automates the entire process on repeat
    def automate(self):
        while True:
            t1 = time.time()
            self.follow_accounts()
            self.unfollow_accounts()

            loop = True
            while loop:

                t2 = time.time()
                if t2 - t1 >3600:
                    loop = False
                else:
                    print(f"{t2-t1} seconds have gone by. {3600-(t2-t1)} seconds left.")
                    time.sleep(2)

if __name__ == "__main__":
    bot = GithubBot()
