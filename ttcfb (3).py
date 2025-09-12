import requests
from time import sleep
from datetime import datetime
import uuid, base64, os, json
from colorama import Fore, init
from rich.console import Console
from pystyle import Colors, Colorate, Write

red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
cam = "\033[38;5;208m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"
thanh = f"{red}[{trang}</>{red}] {trang}=>"
xanh = "\033[1;36m"
gach = f"{trang}-----------------------------------------------------------------"


def _delay(value):
    while not (value <= 1):
        value -= 0.123
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33mX  \033[1;39m ]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m X   \033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}[ \033[1;33m  X  \033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m   X \033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m    X\033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)


def countdown(value):
    while not (value <= 1):
        value -= 0.123
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33mX  \033[1;39m ]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m X   \033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}[ \033[1;33m  X  \033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m   X \033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)
        print(
            f"""\033[1;39m[\033[1;36mMHUNG\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m    X\033[1;39m]""",
            "               ",
            end="\r",
        )
        sleep(0.025)


def decode_base64(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = decoded_bytes.decode("utf-8")
    return decoded_str


def _encode_to_base64(_data):
    byte_representation = _data.encode("utf-8")
    base64_bytes = base64.b64encode(byte_representation)
    base64_string = base64_bytes.decode("utf-8")
    return base64_string


def getid(link):
    getuid = requests.post(
        "https://id.traodoisub.com/api.php", data={"link": link}
    ).json()
    if "success" in getuid:
        return getuid["id"]
    else:
        return False


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        f"""
                      
            {xanh}██╗░░██╗██╗░░░██╗███╗░░██╗░██████╗░
            {trang}██║░░██║██║░░░██║████╗░██║██╔════╝░
            {xanh}███████║██║░░░██║██╔██╗██║██║░░██╗░
            {trang}██╔══██║██║░░░██║██║╚████║██║░░╚██╗
            {xanh}██║░░██║╚██████╔╝██║░╚███║╚██████╔╝
            {trang}╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚═════╝░ 
    """
    )
    print(Colorate.Horizontal(Colors.white_to_blue,"                    © Bản Quyền HMHUNG"))
    print(gach)
    print(f"{thanh}{luc} Admin: {vang}Hà Mạnh Hùng")
    print(f"{thanh}{luc} Facebook: {red}fb.com/hmhung123")
    print(gach)
    sleep(1)


init(autoreset=True)
console = Console()


class Ttc:
    def __init__(self):
        self.__cookie = ""
        self.__headers = {
            "Host": "tuongtaccheo.com",
            "accept": 'application/json, text/javascript, *" . "/" . "*; q=0.01',
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
            "cookie": "",
        }

    def Login(self, token):
        res = requests.post(
            "https://tuongtaccheo.com/logintoken.php", data={"access_token": token}
        )
        if res.json()["status"] == "success":
            self.__cookie = "PHPSESSID=" + (res.cookies)["PHPSESSID"]
            self.__headers["cookie"] = self.__cookie
            user = res.json()["data"]["user"]
            sodu = res.json()["data"]["sodu"]
            return {"user": user, "sodu": sodu}
        else:
            return False

    def CauHinh(self, uid):
        res = requests.post(
            "https://tuongtaccheo.com/cauhinh/datnick.php",
            headers=self.__headers,
            data={"iddat[]": uid, "loai": "fb"},
            timeout=5,
        ).text
        if "1" in res:
            return True
        else:
            return False

    def _GetJob(self, nv):
        get = requests.get(
            f"https://tuongtaccheo.com/kiemtien/{nv}/getpost.php",
            headers=self.__headers,
        )
        return get

    def NhanXu(self, idpost, nv):
        data = {"id": idpost}
        nhan = requests.post(
            f"https://tuongtaccheo.com/kiemtien/{nv}/nhantien.php",
            headers=self.__headers,
            data=data,
        ).json()
        return nhan

    def GetCurrentCoin(self):
        headers = {
            "Host": "tuongtaccheo.com",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
            "cookie": self.__cookie,
        }
        get = requests.get("https://tuongtaccheo.com/home.php", headers=headers).text
        xu = get.split('"soduchinh">')[1].split("<")[0]
        return xu


Ttc = Ttc()

def _Infofb(cookie):
    heads={
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "ProfileCometTimelineListViewRootQuery", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW",
        "Cookie": cookie
    }
    get = requests.get("https://www.facebook.com/me", headers=heads)
    try:
        get = get.url
        get = requests.get(get, headers=heads).text
        _sea = get.split(',"NAME":"')[1].split('",')[0]
        _name = bytes(_sea, "utf-8").decode("unicode_escape")
        _fb1 = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
        _idfb = cookie.split('c_user=')[1].split(';')[0]
        return [_fb1, _idfb, _name]
    except:
        return False



class Cookie:
    def __init__(self):
        self.list = []

    def Input(self):
        print(gach)
        cookie = input(f"{thanh} {luc}Nhập Cookie Facebook Thứ {vang}{len(self.list) + 1}{luc}: {vang}").strip()
        if cookie:
            data = _Infofb(cookie)
            if data:
                print(f"{thanh} {luc}Tên Facebook: {vang}{data[2]}")
                self.list.append(cookie)
                self.Input()
            else:
                print(f"{red}Cookie Facebook Die, Vui Lòng Nhập Lại!!!")
                self.Input()
        with open("cookie_ttcfb.json", "w", encoding="utf-8") as f:
            json.dump(self.list, f, ensure_ascii=False, indent=4)

        if len(self.list) == 0:
            print(f"{red}Nhập ít nhất 1 cookie!!!")
            self.Input()


ck = Cookie()


class Facebook:
    @staticmethod
    def _Like(cookie, uid, type, fb1, idfb):
        headers = {
            "accept": "*/*",
            "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
            "sec-ch-ua-full-version-list": '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Linux"',
            "sec-ch-ua-platform-version": '""',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-asbd-id": "129477",
            "x-fb-friendly-name": "CometUFIFeedbackReactMutation",
            "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW",
        }
        _reac = {
            "LIKE": "1635855486666999",
            "LOVE": "1678524932434102",
            "CARE": "613557422527858",
            "HAHA": "115940658764963",
            "WOW": "478547315650144",
            "SAD": "908563459236466",
            "ANGRY": "444813342392137",
        }
        _id_reac = _reac.get(type)
        _data = {
            "av": idfb,
            "__usid": r"6-Tsfgotwhb2nus:Psfgosvgerpwk:0-Asfgotw11gc1if-RV=6:F=",
            "__aaid": "0",
            "__user": idfb,
            "__a": "1",
            "__req": "2c",
            "__hs": "19896.HYP:comet_pkg.2.1..2.1",
            "dpr": "1",
            "__ccg": "EXCELLENT",
            "__rev": "1014402108",
            "__s": "5vdtpn:wbz2hc:8r67q5",
            "__hsi": "7383159623287270781",
            "__dyn": "7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwKxm5oe8464-5pUfEdK261eBx_wHwdG7FoarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU",
            "__csr": "gug_2A4A8gkqTf2Ih6RFnbk9mBqaBaTs8_tntineDdSyWqiGRYCiPi_SJuLCGcHBaiQXtLpXsyjIymm8oFJswG8CSGGLzAq8AiWZ6VGDgyQiiTBKU-8GczE9USmi4A9DBABHgWEK3K9y9prxaEa9KqQV8qUlxW22u4EnznDxSewLxq3W2K16BxiE5VqwbW1dz8qwCwjoeEvwaKVU6q0yo5a2i58aE7W0CE5O0fdw1jim0dNw7ewPBG0688025ew0bki0cow3c8C05Vo0aNF40BU0rmU3LDwaO06hU06RG6U1g82Bw0Gxw6Gw",
            "__comet_req": "15",
            "fb_dtsg": fb1,
            "jazoest": "25509",
            "lsd": "2JgeTE-rDuLtIVUViHpGjH",
            "__spin_r": "1014402108",
            "__spin_b": "trunk",
            "__spin_t": "1719025807",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "CometUFIFeedbackReactMutation",
            "variables": rf'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{_encode_to_base64("feedback:"+str(uid))}","feedback_reaction_id":"{_id_reac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyxmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{idfb}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}',
            "server_timestamps": "true",
            "doc_id": "7047198228715224",
        }
        cookies = {"cookie": cookie}
        _get = requests.post(
            "https://www.facebook.com/api/graphql/",
            headers=headers,
            cookies=cookies,
            data=_data,
        )
        if '{"data":{"feedback_react":{"feedback":{"id":' in _get.text:
            return True
        else:
            return False

    def _CMT(cookie, id, idfb, fb1, msg: str):
        headers = {
            "accept": "*/*",
            "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
            "sec-ch-ua-full-version-list": '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Linux"',
            "sec-ch-ua-platform-version": '""',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-asbd-id": "129477",
            "x-fb-friendly-name": "CometUFIFeedbackReactMutation",
            "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW",
        }
        _data = {
            "av": idfb,
            "__aaid": "0",
            "__user": idfb,
            "__a": "1",
            "__req": "3a",
            "__hs": "19892.HYP:comet_pkg.2.1..2.1",
            "dpr": "1",
            "__ccg": "GOOD",
            "__rev": "1014295603",
            "__s": "xrpwhz:69a31q:w9xo5s",
            "__hsi": "7381711750373683802",
            "__dyn": "7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewDG1jwUBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azo2NwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWwjHDzUiwRK6E4-8wLwHw",
            "__csr": "gaRMHkaEj4EQgznFON5ifOjsLJA9idO8LqsAHJXeIX48l9lRN4kDmyTAvcKSIAGQtljy9kV4DlGaBAnWUCiqqWmWKA6pBBUymnHBArrCDDKaGaggAQubV8V34iVUCiicoC32Ujm8Ki8H-6UJ1h2KlAyECdg4237CxmQ6F89onXAwjEe8uwxxu5ES2G1qxy3K0xonx21ewnEb8eU2yG2q0hm1yw8G7o7G7oaodU1381T84m0auwdy0dDwb201Z4w2Fo036dg0gYCw2BA0wU7e04WU0qQwlodE04Dq01zOw4Bw51w7hxK",
            "__comet_req": "15",
            "fb_dtsg": fb1,
            "jazoest": "25686",
            "lsd": "H5eT-P3p1zI2ywmbuNcbRm",
            "__spin_r": "1014295603",
            "__spin_b": "trunk",
            "__spin_t": "1718688698",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "useCometUFICreateCommentMutation",
            "variables": rf'{{"feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"groupID":null,"input":{{"client_mutation_id":"4","actor_id":"{idfb}","attachments":null,"feedback_id":"{_encode_to_base64(f"feedback:{id}")}","formatting_style":null,"message":{{"ranges":[],"text":"{msg}"}},"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1718688700413,194880,4748854339,,","vod_video_timestamp":null,"feedback_referrer":"/","is_tracking_encrypted":true,"tracking":["AZX1ZR3ETYfGknoE2E83CrSh9sg_1G8pbUK70jA-zjEIcfgLxA-C9xuQsGJ1l2Annds9fRCrLlpGUn0MG7aEbkcJS2ci6DaBTSLMtA78T9zR5Ys8RFc5kMcx42G_ikh8Fn-HLo3Qd-HI9oqVmVaqVzSasZBTgBDojRh-0Xs_FulJRLcrI_TQcp1nSSKzSdTqJjMN8GXcT8h0gTnYnUcDs7bsMAGbyuDJdelgAlQw33iNoeyqlsnBq7hDb7Xev6cASboFzU63nUxSs2gPkibXc5a9kXmjqZQuyqDYLfjG9eMcjwPo6U9i9LhNKoZwlyuQA7-8ej9sRmbiXBfLYXtoHp6IqQktunSF92SdR53K-3wQJ7PoBGLThsd_qqTlCYnRWEoVJeYZ9fyznzz4mT6uD2Mbyc8Vp_v_jbbPWk0liI0EIm3dZSk4g3ik_SVzKuOE3dS64yJegVOQXlX7dKMDDJc7P5Be6abulUVqLoSZ-cUCcb7UKGRa5MAvF65gz-XTkwXW5XuhaqwK5ILPhzwKwcj3h-Ndyc0URU_FJMzzxaJ9SDaOa9vL9dKUviP7S0nnig0sPLa5KQgx81BnxbiQsAbmAQMr2cxYoNOXFMmjB_v-amsNBV6KkES74gA7LI0bo56DPEA9smlngWdtnvOgaqlsaSLPcRsS0FKO3qHAYNRBwWvMJpJX8SppIR1KiqmVKgeQavEMM6XMElJc9PDxHNZDfJkKZaYTJT8_qFIuFJVqX6J9DFnqXXVaFH4Wclq8IKZ01mayFbAFbfJarH28k_qLIxS8hOgq9VKNW5LW7XuIaMZ1Z17XlqZ96HT9TtCAcze9kBS9kMJewNCl-WYFvPCTCnwzQZ-HRVOM04vrQOgSPud7vlA3OqD4YY2PSz_ioWSbk98vbJ4c7WVHiFYwQsgQFvMzwES20hKPDrREYks5fAPVrHLuDK1doffY1hPTWF2KkSt0uERAcZIibeD5058uKSonW1fPurOnsTpAg8TfALFu1QlkcNt1X4dOoGpYmBR7HGIONwQwv5-peC8F758ujTTWWowBqXzJlA2boriCvdZkvS15rEnUN57lyO8gINQ5heiMCQN8NbHMmrY_ihJD3bdM4s2TGnWH4HBC2hi0jaIOJ8AoCXHQMaMdrGE1st7Y3R_T6Obg6VnabLn8Q-zZfToKdkiyaR9zqsVB8VsMrAtEz0yiGpaOF3KdI2sxvii3Q5XWIYN6gyDXsXVykFS25PsjPmXCF8V1mS7x6e9N9PtNTWwT8IGBZp9frOTQN2O52dOhPdsuCHAf0srrBVHbyYfCMYbOqYEEXQG0pNAmG_wqbTxNew9kTsXDRzYKW-NmEJcvy_xh1dDwg8xJc58Cl71e-rau3iP7o8mWhVSaxi4Bi6LAuj4UKVCt3IYCfm9AR1d5LqBFWU9LrJbRZSMlmUYwZf7PlrKmpnCnZvuismiL7DH3cnUjP0lWAvhy3gxZm1MK8KyRzWmHnTNqaVlL37c2xoE4YSyponeOu5D-lRl_Dp_C2PyR1kG6G0TCWS66UbU89Fu1qmwWjeQwYhzj2Jly9LRyClAbe86VJhIZE18YLPB-n1ng78qz7hHtQ8qT4ejY4csEjSRjjnHdz8U-06qErY-CXNNsVtzpYGuzZ1ZaXqzAQkUcREm98KR8c1vaXaQXumtDklMVgs76gLqZyiG1eCRbOQ6_EcQv7GeFnq5UIqoMH_Xzc78otBTvC5j3aCs5Pvf6k3gQ5ZU7E4uFVhZA7xoyD8sPX6rhdGL8JmLKJSGZQM5ccWpfpDJ5RWJp0bIJdnAJQ8gsYMRAI2OBxx2m2c76lNiUnB750dMe2H3pFzFQVkWQLkmGVY37cgmRNHyXboDMQ1U2nlbNH017dmklJCk4jVU8aA9Gpo8oHw","{{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":\"{uuid.uuid4()}\",\"conversation_guide_shown\":null}}"],"feedback_source":"DEDICATED_COMMENTING_SURFACE","idempotence_token":"client:{uuid.uuid4()}","session_id":"{uuid.uuid4()}"}},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null}}',
            "server_timestamps": "true",
            "doc_id": "7994085080671282",
        }
        cookies = {"cookie": cookie}
        try:
            _get = requests.post(
                "https://www.facebook.com/api/graphql/",
                headers=headers,
                cookies=cookies,
                params=_data,
            )
            if '"errors"' not in _get.text:
                return True
            else:
                return False
        except:
            return False


def chongblock(delaybl):
    for i in range(delaybl, -1, -1):
        Write.Print(
            f"Đang ở chế độ chống block, sẽ chạy lại sau {i} giây  \r",
            Colors.rainbow,
            interval=0.0001,
        )
        sleep(1)
        print("                                                        ", end="\r")


def Main():
    mhung = False
    banner()
    user, sodu, token_list = "", 0, []

    def choose():
        nonlocal user, sodu, token_list

        def load_tokens():
            with open("token_ttcfb.json", "r") as f:
                data = json.loads(f.read())
                return [
                    {"user": tk.split("|", 1)[0], "token": tk.split("|", 1)[1]}
                    for tk in data
                ]

        def select_token(token_list):
            for idx, tk in enumerate(token_list, start=1):
                print(
                    f'{thanh} {luc}Account {red}[{vang}{idx}{red}] {luc}Để chạy tài Khoản: {vang}{tk["user"]}'
                )

            print(gach)
            print(
                f"{thanh}{luc} {red}[{vang}1{red}] {luc}Chọn Acc Tương Tác Chéo Đã Lưu"
            )
            print(f"{thanh}{luc} {red}[{vang}2{red}] {luc}Để Nhập Access_Token TTC Mới")
            print(gach)
            while True:
                choice = input(f"{thanh}{luc} Nhập: {vang}").strip()

                if choice == "1":
                    print(gach)
                    while True:
                        try:
                            selected = int(input(f"{thanh}{luc} Nhập số Acc: {vang}"))
                            if 1 <= selected <= len(token_list):
                                return token_list[selected - 1]["token"]
                            else:
                                print(f"{red}Số Acc Không Tồn Tại")
                        except ValueError:
                            print(gach)
                            print(f"{red}Vui Lòng Nhập Số Hợp Lệ!!!")

                elif choice == "2":
                    print(gach)
                    while True:
                        token = input(f"{thanh}{luc} Nhập Token TTC: {vang}").strip()
                        if token in [t["token"] for t in token_list]:
                            print(gach)
                            print(f"{red}Token Đã Tồn Tại!!!")
                        else:
                            return token
                else:
                    print(gach)
                    print(f"{red}Vui Lòng Nhập Chính Xác")

        def load_cookies():
            with open("cookie_ttcfb.json", "r") as f:
                try:
                    return json.loads(f.read())
                except:
                    os.remove("cookie_ttcfb.json")
                    return []

        def handle_cookies():
            print(f"{thanh} {red}[{vang}1{red}] {luc}Sử Dụng Cookie Facebook Đã Lưu")
            print(f"{thanh} {red}[{vang}2{red}] {luc}Nhập Cookie Facebook Mới")
            print(gach)
            while True:
                choice = input(f"{thanh}{luc} Lựa Chọn Của Bạn: {vang}")
                if choice == "1":
                    print(f"{trang}Đang Lấy Dữ Liệu Đã Lưu...")
                    sleep(1)
                    ck.list = load_cookies()
                    break
                elif choice == "2":
                    ck.Input()
                    break
                else:
                    print(f"{red}Lựa Chọn Không Hợp Lệ, Vui Lòng Nhập Lại!!!")
                    continue

        if os.path.exists("token_ttcfb.json"):
            banner()
            token_list = load_tokens()
            token = select_token(token_list)
        else:
            token = input(f"{thanh} {luc}Nhập Token TTC: {trang}")

        data = Ttc.Login(token)
        if data:
            user = data["user"]
            sodu = data["sodu"]
            if not token in [token["token"] for token in token_list]:
                token_list.append({"user": user, "token": token})
                with open("token_ttcfb.json", "w") as f:
                    f.write(
                        json.dumps(
                            [f"{tk['user']}|{tk['token']}" for tk in token_list],
                            ensure_ascii=False,
                            indent=4,
                        )
                    )
        else:
            print(f"{thanh}{red} Token TTC Không Hợp Lệ, Vui Lòng Nhập Lại!!!")
            exit(1)
        if os.path.exists("cookie_ttcfb.json"):
            banner()
            handle_cookies()
        else:
            ck.Input()

    choose()
    banner()
    print(gach)
    print(f"{thanh} {luc}Tên Tài Khoản: {vang}{user} {luc}")
    print(f"{thanh} {luc}Xu Hiện Tại: {vang}{sodu}")
    print(f"{thanh} {luc}Số Cookie Facebook: {vang}{len(ck.list)}")
    print(gach)
    print(f"{thanh} {luc}Nhập {red}[{vang}1{red}]{luc} Để Chạy Nhiệm Vụ Like Thường")
    print(f"{thanh} {luc}Nhập {red}[{vang}2{red}]{luc} Để Chạy Nhiệm Vụ Like Vip")
    print(f"{thanh} {luc}Nhập {red}[{vang}3{red}]{luc} Để Chạy Nhiệm Vụ Cảm Xúc Vip")
    print(f"{thanh} {luc}Nhập {red}[{vang}4{red}]{luc} Để Chạy Nhiệm Vụ Cảm Xúc Thường")
    print(f"{thanh} {luc}Nhập {red}[{vang}5{red}]{luc} Để Chạy Nhiệm Vụ Comment")
    print(gach)
    nhiemvu = input(f"{thanh}{luc} Nhập Nhiệm Vụ Cần Chạy: {vang}")
    delay = int(input(f"{thanh}{luc} Nhập Delay: {vang}"))
    nvblock = int(input(f"{thanh}{luc} Sau Bao Nhiêu Job thì Chống Block: {vang}"))
    delay_block = int(input(f"{thanh}{luc} Sau {vang}{nvblock}{luc} Job Nghỉ Bao Nhiêu Giây: {vang}"))
    job_doiacc = int(input(f"{thanh}{luc} Sau Bao Nhiêu Job Đổi Acc: {vang}"))
    b = input(f"{thanh}{luc} Bạn Có Muốn Ẩn Id Không? {red}({vang}y{trang}/{vang}n{red}){luc}: {vang}")
    anid = b.lower() == "y"
    dem = 0
    totalcoin = 0
    mhung = False

    while True:
        err = 0
        if len(ck.list) == 0:
            print(f"{red}Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại")
            ck.Input()
        for cookie in ck.list:
            loilikere, loilikevip, loireactvip, loireactre, loicomment = 0, 0, 0, 0, 0
            info = _Infofb(cookie)
            if info:
                fb_dtsg = info[0]
                uidfb = info[1]
                namefb = info[2]
            else:
                uidfb = cookie.split("c_user=")[1].split(";")[0]
                print(f"{red}Cookie Tài Khoản {uidfb} Die")
                sleep(3)
                ck.list.remove(cookie)
                continue

            cauhinh = Ttc.CauHinh(uidfb)
            if cauhinh:
                print(
                    f"{luc}ID Facebook: {vang}{uidfb[:4] + '#'*(len(uidfb)-7) + uidfb[-3:] if anid else uidfb} "
                    f"{red}| {luc}Tên Facebook: {vang}{namefb.encode('utf-8', 'replace').decode()}"
                )

            else:
                print(f"{luc}Chưa Cấu Hình ID: {vang}{uidfb} {red}| {luc}Tên Facebook: {vang}{namefb}")
                ck.list.remove(cookie)
                continue

            while True:
                nvlike = "1" in nhiemvu
                nvlikevip = "2" in nhiemvu
                nvreactvip = "3" in nhiemvu
                nvreact = "4" in nhiemvu
                nvcomment = "5" in nhiemvu

                if nvlike:
                    nv = "likepostvipre"
                    job = Ttc._GetJob(nv).json()
                    if not job:
                        print(
                            f"{luc}Hết Nhiệm Vụ {nv}                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        nvlike = False
                    elif "error" in job:
                        print(
                            f"{luc}Lấy nhiệm vụ sau 10 giây                    ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        countdown(10)
                        nvlike = False
                    else:
                        print(
                            f"{luc}Tìm Thấy {vang}{len(job)} {luc}Nhiệm Vụ {nv}                      ",
                            end="\r",
                        )
                        for x in job:
                            try:
                                idpost = x["idpost"]
                                id = x["idfb"]
                            except KeyError:
                                countdown(6)
                                continue

                            like = Facebook._Like(cookie, id, "LIKE", fb_dtsg, uidfb)
                            if not like:
                                loilikere += 1
                                err += 1
                                print(
                                    f"{trang}[{red}{err}{trang}] [{red}ERROR{trang}] {id}             ", end="\r"
                                )
                                sleep(2)
                            else:
                                nhan = Ttc.NhanXu(idpost, nv)
                                if "mess" in nhan:
                                    xu = Ttc.GetCurrentCoin()
                                    dem += 1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(
                                        f'{red}| {vang}{dem}{red} | {xanh}{time}{red} | {vang}LIKE{red} | {trang}{id}{red} | {vang}+400{red} | {luc}{str(format(int(xu), ","))}'
                                    )
                                    loilikere = 0
                                    err = 0
                                    totalcoin += 400
                                    if dem % 10 == 0:
                                        print(
                                            f"{trang}[{luc}Total Cookie Facebook: {vang}{len(ck.list)}{trang}] [{luc}Total Coin: {vang}{str(format(int(totalcoin), ','))}{trang}] [{luc}Tổng Xu: {vang}{str(format(int(xu), ','))}{trang}]"
                                        )
                                    if dem % job_doiacc == 0:
                                        mhung = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delay_block)
                                    else:
                                        _delay(delay)

                            if loilikere >= 20:
                                _info = _Infofb(cookie)
                                if not _info:
                                    print(
                                        f"{red}Cookie Tài Khoản {vang}{namefb}{red} Đã Bị Out !!!                "
                                    )
                                    ck.list.remove(cookie)
                                else:
                                    print(
                                        f"{red}Tài Khoản {trang}{namefb} {red}Đã Bị Block {trang}{nv} {red}!!!					"
                                    )
                                    nvlike = False
                                mhung = True
                                break

                        if mhung:
                            break

                if nvlikevip:
                    nv = "likepostvipcheo"
                    job = Ttc._GetJob(nv).json()
                    if not job:
                        print(
                            f"{luc}Hết Nhiệm Vụ {nv}                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        nvlikevip = False
                    elif "error" in job:
                        print(
                            f"{luc}Lấy nhiệm vụ sau 10 giây                    ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        countdown(10)
                        nvlikevip = False
                    else:
                        print(
                            f"{luc}Tìm Thấy {vang}{len(job)} {luc}Nhiệm Vụ {nv}                      ",
                            end="\r",
                        )
                        for x in job:
                            try:
                                idpost = x["idpost"]
                                id = x["idfb"]
                            except KeyError:
                                countdown(6)
                                continue

                            like = Facebook._Like(cookie, id, "LIKE", fb_dtsg, uidfb)
                            if not like:
                                loilikevip += 1
                                err += 1
                                print(
                                    f"{trang}[{red}{err}{trang}] [{red}ERROR{trang}] {id}             ", end="\r"
                                )
                                sleep(2)
                            else:
                                nhan = Ttc.NhanXu(idpost, nv)
                                if "mess" in nhan:
                                    xu = Ttc.GetCurrentCoin()
                                    dem += 1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(
                                        f'{red}| {vang}{dem}{red} | {xanh}{time}{red} | {vang}LIKE{red} | {trang}{id}{red} | {vang}+1100{red} | {luc}{str(format(int(xu), ","))}'
                                    )
                                    loilikevip = 0
                                    err = 0
                                    totalcoin += 1100
                                    if dem % 10 == 0:
                                        print(
                                            f"{trang}[{luc}Total Cookie Facebook: {vang}{len(ck.list)}{trang}] [{luc}Total Coin: {vang}{str(format(int(totalcoin), ','))}{trang}] [{luc}Tổng Xu: {vang}{str(format(int(xu), ','))}{trang}]"
                                        )
                                    if dem % job_doiacc == 0:
                                        mhung = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delay_block)
                                    else:
                                        _delay(delay)

                            if loilikevip >= 20:
                                _info = _Infofb(cookie)
                                if not _info:
                                    print(
                                        f"{red}Cookie Tài Khoản {vang}{namefb}{red} Đã Bị Out !!!                "
                                    )
                                    ck.list.remove(cookie)
                                else:
                                    print(
                                        f"{red}Tài Khoản {trang}{namefb} {red}Đã Bị Block {trang}{nv} {red}!!!					"
                                    )
                                    nvlikevip = False
                                mhung = True
                                break

                        if mhung:
                            break

                if nvreactvip:
                    nv = "camxucvipcheo"
                    job = Ttc._GetJob(nv).json()
                    if not job:
                        print(
                            f"{luc}Hết Nhiệm Vụ {nv}                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        nvreactvip = False
                    elif "error" in job:
                        print(
                            f"{luc}Lấy nhiệm vụ sau 10 giây                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        countdown(10)
                        nvreactvip = False
                    else:
                        print(
                            f"{luc}Tìm Thấy {lam}{len(job)} {luc}Nhiệm Vụ {nv}                       ",
                            end="\r",
                        )
                        for x in job:
                            try:
                                idpost = x["idpost"]
                                id = x["idfb"]
                                type = x["loaicx"]
                            except KeyError:
                                countdown(6)
                                continue

                            like = Facebook._Like(cookie, id, type, fb_dtsg, uidfb)
                            if not like:
                                loireactvip += 1
                                err += 1
                                print(
                                    f"{trang}[{red}{err}{trang}] [{red}ERROR{trang}] {id}             ", end="\r"
                                )
                                sleep(2)
                            else:
                                nhan = Ttc.NhanXu(idpost, nv)
                                if "mess" in nhan:
                                    xu = Ttc.GetCurrentCoin()
                                    dem += 1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(
                                        f'{red}| {vang}{dem}{red} | {xanh}{time}{red} | {vang}{type}{red} | {trang}{id}{red} | {vang}+1100{red} | {luc}{str(format(int(xu), ","))}'
                                    )
                                    loireactvip = 0
                                    err = 0
                                    totalcoin += 1100
                                    if dem % 10 == 0:
                                        print(
                                            f"{trang}[{luc}Total Cookie Facebook: {vang}{len(ck.list)}{trang}] [{luc}Total Coin: {vang}{str(format(int(totalcoin), ','))}{trang}] [{luc}Tổng Xu: {vang}{str(format(int(xu), ','))}{trang}]"
                                        )
                                    if dem % job_doiacc == 0:
                                        mhung = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delay_block)
                                    else:
                                        _delay(delay)

                            if loireactvip >= 20:
                                _info = _Infofb(cookie)
                                if not _info:
                                    print(
                                        f"{red}Cookie Tài Khoản {vang}{namefb}{red} Đã Bị Out !!!                "
                                    )
                                    ck.list.remove(cookie)
                                else:
                                    print(
                                        f"{red}Tài Khoản {vang}{namefb} {red}Đã Bị Block {vang}{nv} {red}!!!					"
                                    )
                                    nvreactvip = False
                                mhung = True
                                break

                if nvreact:
                    nv = "camxucvipre"
                    job = Ttc._GetJob(nv).json()
                    if not job:
                        print(
                            f"{luc}Hết Nhiệm Vụ {nv}                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        nvreact = False
                    elif "error" in job:
                        print(
                            f"{luc}Lấy nhiệm vụ sau 10 giây                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        countdown(10)
                        nvreact = False
                    else:
                        print(
                            f"{luc}Tìm Thấy {lam}{len(job)} {luc}Nhiệm Vụ {nv}                       ",
                            end="\r",
                        )
                        for x in job:
                            try:
                                idpost = x["idpost"]
                                id = x["idfb"]
                                type = x["loaicx"]
                            except KeyError:
                                countdown(6)
                                continue

                            like = Facebook._Like(cookie, id, type, fb_dtsg, uidfb)
                            if not like:
                                loireactre += 1
                                err += 1
                                print(
                                    f"{trang}[{red}{err}{trang}] [{red}ERROR{trang}] {id}             ", end="\r"
                                )
                                sleep(2)
                            else:
                                nhan = Ttc.NhanXu(idpost, nv)
                                if "mess" in nhan:
                                    xu = Ttc.GetCurrentCoin()
                                    dem += 1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(
                                        f'{red}| {vang}{dem}{red} | {xanh}{time}{red} | {vang}{type}{red} | {trang}{id}{red} | {vang}+400{red} | {luc}{str(format(int(xu), ","))}'
                                    )
                                    loireactre = 0
                                    err = 0
                                    totalcoin += 400
                                    if dem % 10 == 0:
                                        print(
                                            f"{trang}[{luc}Total Cookie Facebook: {vang}{len(ck.list)}{trang}] [{luc}Total Coin: {vang}{str(format(int(totalcoin), ','))}{trang}] [{luc}Tổng Xu: {vang}{str(format(int(xu), ','))}{trang}]"
                                        )
                                    if dem % job_doiacc == 0:
                                        mhung = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delay_block)
                                    else:
                                        _delay(delay)

                            if loireactre >= 20:
                                _info = _Infofb(cookie)
                                if not _info:
                                    print(
                                        f"{red}Cookie Tài Khoản {vang}{namefb}{red} Đã Bị Out !!!                "
                                    )
                                    ck.list.remove(cookie)
                                else:
                                    print(
                                        f"{red}Tài Khoản {vang}{namefb} {red}Đã Bị Block {vang}{nv} {red}!!!					"
                                    )
                                    nvreact = False
                                mhung = True
                                break

                        if mhung:
                            break
                if nvcomment:
                    nv = "cmtcheo"
                    job = Ttc._GetJob(nv).json()
                    if not job:
                        print(
                            f"{luc}Hết Nhiệm Vụ {nv}                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        nvcomment = False
                    elif "error" in job:
                        print(
                            f"{luc}Lấy nhiệm vụ sau 10 giây                            ",
                            end="\r",
                        )
                        sleep(2)
                        print(
                            "                                                        ",
                            end="\r",
                        )
                        countdown(10)
                        nvcomment = False
                    else:
                        print(
                            f"{luc}Tìm Thấy {vang}{len(job)} {luc}Nhiệm Vụ {nv}                       ",
                            end="\r",
                        )
                        for x in job:
                            try:
                                idpost = x["idpost"]
                                nd = json.loads(x["nd"])[0]
                            except KeyError:
                                countdown(6)
                                continue
                            cmt = Facebook._CMT(cookie, idpost, uidfb, fb_dtsg, nd)
                            if not cmt:
                                loicomment += 1
                                err += 1
                                print(
                                    f"{trang}[{red}{err}{trang}] [{red}ERROR{trang}] {idpost}             ", end="\r"
                                )
                                sleep(2)
                            else:
                                nhan = Ttc.NhanXu(idpost, nv)
                                if "mess" in nhan:
                                    xu = Ttc.GetCurrentCoin()
                                    dem += 1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(
                                        f'{red}| {vang}{dem}{red} | {xanh}{time}{red} | {vang}CMT{red} | {trang}{idpost}{red} | {vang}+1400{red} | {luc}{str(format(int(xu), ","))}'
                                    )
                                    loicomment = 0
                                    err = 0
                                    totalcoin += 1400
                                    if dem % 10 == 0:
                                        print(
                                            f"{trang}[{luc}Total Cookie Facebook: {vang}{len(ck.list)}{trang}] [{luc}Total Coin: {vang}{str(format(int(totalcoin), ','))}{trang}] [{luc}Tổng Xu: {vang}{str(format(int(xu), ','))}{trang}]"
                                        )
                                    if dem % job_doiacc == 0:
                                        mhung = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delay_block)
                                    else:
                                        _delay(delay)

                            if loicomment >= 20:
                                _info = _Infofb(cookie)
                                if not _info:
                                    print(
                                        f"{red}Cookie Tài Khoản {vang}{namefb}{red} Đã Bị Out !!!                "
                                    )
                                    ck.list.remove(cookie)
                                else:
                                    print(
                                        f"{red}Tài Khoản {vang}{namefb} {red}Đã Bị Block {lam}{nv} {red}!!!					"
                                    )
                                    nvcomment = False
                                mhung = True
                                break
                        if mhung:
                            break


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print(f"\n{red}Đã Dừng Tool")
        exit(0)