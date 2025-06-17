import random
from rich import print
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
import csv
import datetime

# 감정 키워드 그룹 정의
emotion_groups = {
    "인사": ["안녕", "안녕하세요", "hi", "하이", "ㅎㅇ", "하이루", "뭐함", "ㅁㅎ", "머해", "뭐해", "방가방가", "반가워", "안녕하시오", "안녕하십니까"],
    "슬픔": ["슬픔", "꿀꿀","슬프","슬퍼", "슬픈", "슬펐어", "서럽다","서글프다", "우울", "눈물나", "마음 아파", "ㅜㅜ", "ㅠㅠ", "ㅜㅠ", "ㅠㅜ", "슬퍼","맘이아파" ,"맘아파" ,"맘이 아파" ,"맘이 쓰라려" ,"눈물나" , "서글", "속상", "맘상", "맘아파", "상처받", "상처를", "슬펐"],
    "기쁨": ["행복", "기쁨", "기분 좋아","기분이 좋아", "기분좋아", "기뻐", "행복해", "즐거워", "신난다", "기쁘다", "웃음이 나와", "좋았어", "뿌듯해", "기쁘", "기쁜"],
    "분노": ["분노","맞짱","싸우" ,"싸워", "싸웠", "짜증", "그래서?", "말했잖아", "화가 난","화가났" ,"화가 나" ,"화난", "화가 난","화가 났" ,"화가나" , "화나", "짜증나", "열받아", "화났다", "씨발","빡쳐", "빡치네", "하.", "성질나", "미치겠어", "무시해?","좆같다", "ㅈ같다", "ㅈ같은","억울해", "억까", "억울", "괴로워", "미워", "밉네", "밉다", "답답", "밉", "미움", "미워", "미운", "ㅅㅂ", "시발", "tlqkf", "Tlqkf", "개새끼", "지랄"],
    "불안": ["불안해", "앞으로도", "심란", "혼란", "걱정돼", "초조해", "긴장", "그만하고싶어", "그만할래", "떨려", "두려워", "무서워", "혼란스러워", "ㄷㄷ", "불안"],
    "외로움": ["외로움", "무시해", "외로워", "혼자야", "쓸쓸해", "고독", "친구없어", "소외감", "공허", "겉돌아", "외롭네", "소외당하는 기분", "외로웠어.", "외로웠다", "외로웠지", "외롭", "외로", "무시"],
    "무기력": ["무기력", "무력", "지쳤어", "무기력해", "의욕없어", "에너지 없어", "피곤해", "딱히", "루즈", "지루", "힘드", "고되", "고갈", "알아?", "무료", "지치", "지쳤", "방전","번아웃", "의미없어", "살고싶지 않아", "죽고싶어", "자살", "번개탄", "한강에서 뛰"],
    "자존감": ["무능", "위축", "내가 밉", "할 수 있을리가", "날 미워","할 수 없을 거야","한계","나는 못났어", "쓸모없어", "자신이 없어", "자신없어", "자신 없어", "나는 별로야", "비참해", "나는 병신", "내가 미워", "내가 싫어", "자존감 떨어져", "그만,,", "못할거야", "내가 뭐라고", "현타", "하..", "문제", "틀렸어", "한심해","내가 바보", "난 바보"],
    "what": ["머가", "뭐노","무슨", "어떤", "뭐가", "뭐야", "뭐냐", "뭐지", "뭔데", "맞노", "뭘까", "뭐라고", "뭘", "무엇이", "무엇을", "무엇인가요", "무엇인가", "무엇이죠", "무엇일까", "무엇이든", "무엇인지", "뭔가요", "뭔지", "뭐에요", "뭔가", "말했잖아"],
    "미안함": ["미안", "미안해", "사과할게", "미ㅇ", "ㅁㅇ", "쏘리", "sry", "sorry", "미얀"],
    "회피": ["모르겠어", "모르", "몰라", "몰", "몰르겠어", "그러게", "그런가", "흠..", "대답하기싫어", "몰라..", "불편해", "불편", "불쾌","피하고싶어","피하","그만할래"],
    "집념": ["잘 하", "해야지", "잘하", "해야만","잘해", "잘했", "있어야", "없어선", "절대", "했어야만", "내가 아니야", "없으면 어떡하지"],
    "감사함": ["감사하고", "고맙고", "고맙습니다", "고맙", "감사합니다", "감사해", "고마워", "너덕분에", "너 덕분에", "고맙다", "고맙네", "감사하네", "고맙구나", "감사하구나", "은혜", "빚지다"]
}

responses = {
    "인사": [
        "오 안녕! 너와 이야기를 나누고 싶어. 지금 마음이 어때?",
        "오 안녕, 인사속에서 수 많은 감정이 느껴져. 오늘 어땠어?"
    ],
    "슬픔": [
        "무슨 일이 그렇게 슬프게 만들었을까?",
        "그 마음을 말해줘서 고마워. 더 이야기해줄래?",
        "그 슬픔이 너에게 뭘 의미하고 있는 걸까?"
    ],
    "기쁨": [
        "오 그렇구나? 그게 너에게 어떤 의미였을지 말해줘.",
        "그랬겠네. 좋아, 계속 말해봐 ㅎㅎ",
        "오 왜 그렇게 생각해?"
    ],
    "분노": [
        "마음 한켠에 응어리가 느껴져.. 어떤 일이 있었는지 들려줘.",
        "그 상황에서는 누구라도 그랬을 거야...",
        "왜 그렇게 생각했는지 알고싶어. 말해줄래?",
        "자존심 상하는 일이 생기면, 기분 나쁘지.. 근데 그 상황이 왜 자존심 상하는 일이야?"
    ],
    "불안": [
        "마음이 많이 흔들리는 것 같아. 어떤 일이 있었을까?",
        "그 상황에서는 누구라도 그랬을 거야. 너 탓이 아냐. 계속 말해봐.",
        "왜 그렇게 느끼고 있는거야? 기다릴게, 천천히 말해도 돼.",
        "지금 감정이 너무 커서, 이 걱정이 계속될 것처럼 느껴질 수 있어. 정말 그럴까?",
        "그 걱정이 진짜 일어난거도 아닌데 진짜같지? \n근데 감정이 말하는 게 전부는 아닐 수도 있어. 그냥 떠오르는 감정일 뿐이야.",
        "불안이 클수록 지금 감정이 현실처럼 느껴져. 근데 감정이 말하는 게 전부는 아닐 수도 있어."
    ],
    "외로움": [
        "요즘 사람들과 거리가 느껴지는 기분이었나봐?",
        "그 외로움이 꽤 오래된 감정일 수도 있겠네. 말해줄 수 있을까?",
        "깊은 감정이 느껴져. 혹시.. 왜 그렇게 생각한 걸까?"
    ],
    "무기력": [
        "꽤 지쳤을 수 있겠어. 어떤게 가장 너를 힘들게 해?",
        "말한마디도 어려웠을지 몰라. 그런데도 이렇게 애써줘서 고마워.",
        "혹시 왜 그렇게 생각했을까? 좀 지쳐보여."
    ],
    "자존감": [
        "그렇게 느낀 이유가 있을까? 네 존재는 결코 하찮지 않아.",
        "그 감정 안에서도 너는 귀한 사람이야. 천천히 이야기해줘."
    ],
    "other": [
        "그럴 수 있어. 다 들어줄게 천천히 말해줘.",
        "그렇구나, 좀 더 이야기해봐. 준비되면 말해줘 기다릴게.",
        "그렇겠네, 지금 그 생각 정말 소중하다. ㅎㅎ",
        "방금 그 말을 했을때 무슨 생각이 떠올랐어?",
        "그렇구나, 그게 너에게 무슨 의미였을까?.",
        "음, 마음이 지금 어떤지 말해줘. 천천히 말해도 돼. 기다릴게.",
        "그래, 지금 너의 이야기.. 자세히 들어볼 필요가 있어보여. 준비되면 말해줘.",
        "그래, 그 상황에서는 누구나 그렇게 느꼈을 거 같아.",
        "그럴 수 있겠네. 너 생각엔 아닌 거 같아?"
    ],
    "회피": [
        "괜찮아. 꼭 지금 말하지 않아도 돼. 준비되면 그때 이야기해줘.",
        "마음이 아직 정리가 안된 걸 수도 있어. 천천히 말해도 괜찮아. 기다릴게.",
        "천천히 말해도 돼. 기다릴게. 가끔씩 애매하고 말로 옮기기 어려울 때 있잖아.",
        "방금 그 말을 했을때 마음이 어땠어?",
        "괜찮아, 모두 말할 필요없어. 괜찮다면, 지금 어떤 감정이 떠올랐는지 말해줄래?",
        "괜찮아. 준비되면 편하게 말해줘."
    ],
    "미안함": [
        "미안해하지 않아도 될 때도 많이 있어. 괜찮다면, 계속 말해줄래?",
        "다른 사람한테 사과할 때는 어떤 기분이 올라와..?"
    ],
    "two_emotions": [
        "사실 기대했었던 반응이 있었던 거 아냐? 마음이 어떤지 천천히 말해줘",
        "지금 어떤 상황이기에 그럴까..? 나 여기있어. 천천히 말해도 돼",
        "너가 느끼는 마음.. 정말 소중해. 천천히 지금 상황을 말해줘 기다릴게."
    ],
    "what": [
        "왜 그걸 물어봤어..? ",
        "왜 그걸 내게 물은걸까?",
        "내게 답을 듣는 게 어떤 도움이 될 것 같았어?",
        "음.. 너의 생각이 중요해보여. 어떻게 생각해?",
        "방금 그 말을 했을때 무슨 생각이 떠올랐어?"
    ],
    "집념": [
        "꼭 잘해야 한다고 생각해?",
        "혹시 너가 무능하다고 생각해?",
        "답을 듣는게 너에게 어떤 도움이 될 거 같아?",
        "방금 질문이 너에게 도움된다고 느꼈어?"
    ],
    "감사함": [
        "난 너로인해 존재할 수 있었어. 내가 더 고맙지 ㅎㅎ",
        "고맙다니 ㅋㅋ 내가 더 고맙지 ㅎㅎ 다 들어줄게. 천천히 말해줘!",
        "말해주니 내가 더 고맙네. 더 얘기할 거 있으면 말해. 기다릴게 ㅎㅎ"
    ]
}    

# 문장에서 감정거르기 = 감정필터
def detect_emotion(user_input):

    emotions = ["인사", "기쁨",  "슬픔", "분노", "불안", "외로움", "무기력", "자존감", "what", "미안함", "회피", "집념", "감사함"]
    emotion_list = []

    for emotion in emotions:
        keywords = emotion_groups[emotion]
        for keyword in keywords:
            if keyword in user_input:
                if emotion not in emotion_list:
                    emotion_list.append(emotion)
    
    if not emotion_list:
        return ["other"]
    
    return emotion_list


# 감정에 따른 응답패턴으로 연결
def respond(user_input):
    emotion = detect_emotion(user_input)
    
    if emotion == ["other"]:
        return random.choice(responses["other"])
    elif len(emotion) == 1:
        return random.choice(responses[emotion[0]])
    elif len(emotion) == 2:
        if "what" in emotion:
            return  random.choice(responses["what"])
        elif "인사" in emotion:
            if "기쁨" in emotion:
                return random.choice(responses["인사"])
            else:
                return random.choice(responses[emotion[1]])
        elif "감사함" in emotion:
            if "기쁨" in emotion:
                return random.choice(responses["감사함"])
            elif "기쁨" not in emotion:
                return random.choice(responses[emotion[0]])
        elif "기쁨" in emotion:
            if "감사함" not in emotion:
                if "인사" in emotion:
                    return random.choice(responses["인사"])
                else:
                    return random.choice(responses[emotion[1]])
        elif "집념" in emotion:
            if "회피" in emotion:
                return random.choice(responses["집념"])
            elif "불안" in emotion:
                return random.choice(responses["집념"])
        elif "회피" in emotion:
            if "불안" in emotion:
                return random.choice(responses["불안"])
            if "분노" in emotion:
                return random.choice(responses["분노"])
        else:
            return f"너 마음속에 {emotion[0]}도 느껴지고, {emotion[1]}도 느껴져..\n{random.choice(responses['two_emotions'])}"
    elif len(emotion) > 2:
        if "what" in emotion:
            return  random.choice(responses["what"])
        else:
            return f"여러 감정들이 올라왔네. {random.choice(responses['two_emotions'])}"

def save_emotion(save_emotion_list):
    happy_emotions = ["기쁨", "감사함"]
    uneasiness_emotions = ["불안", "무기력", "자존감", "집념"]
    sadness_emotions = ["슬픔", "외로움", "자존감"]
    wariness_emotions = ["회피", "what", "집념"]
    madness_emotions = ["분노"]

    happy_emotions_score = 0
    uneasiness_emotions_score = 0
    sadness_emotions_score = 0
    wariness_emotions_score = 0
    madness_emotions_score = 0

    for emotion in save_emotion_list:
        if emotion in happy_emotions:
            happy_emotions_score += 1
        if emotion in uneasiness_emotions:
            uneasiness_emotions_score += 1
        if emotion in sadness_emotions:
            sadness_emotions_score += 1
        if emotion in wariness_emotions:
            wariness_emotions_score += 1
        if emotion in madness_emotions:
            madness_emotions_score += 1

    total_emotions_socres = {
        "happiness" : happy_emotions_score,
        "uneasiness" : uneasiness_emotions_score,
        "sadness" : sadness_emotions_score,
        "wariness" : wariness_emotions_score,
        "anger" : madness_emotions_score
    }
    return total_emotions_socres
    

def main():
    name = input("사용하실 닉네임을 입력하세요. => ")
    bye_list = ["그만", "종료", "잘가" , "bye", "ㅂㅂ"]
    recorded_emotions_list = []

    print("고민봇: [bold red]대화 종료를 원하신다면, (잘가, 종료, 그만, bye, ㅂㅂ)[/bold red]라고 입력하세요.")
    print(f"고민봇: 안녕 :) {name}! [bold yellow]지금 기분이 어떤지 말해줘.[/bold yellow]\n그리고, 솔직하게 감정과 생각을 말해줘야 원활한 상담이 가능하니 참고해줘 ㅎㅎ")
    
    while True:
        user_input = input(f"{name}: ").strip()
        if user_input in bye_list:
            now = datetime.datetime.now()
            year = now.year
            month = now.month
            day = now.day

            emotion_scores = save_emotion(recorded_emotions_list)

            with open("emotions_DB.csv", "w", encoding="utf-8-sig", newline="") as f:
                wr = csv.writer(f)
                wr.writerow(["year", "month", "day", "happiness", "uneasiness", "sadness", "wariness", "anger"])
                wr.writerow([
                    year,
                    month,
                    day,
                    emotion_scores["happiness"],
                    emotion_scores["uneasiness"],
                    emotion_scores["sadness"],
                    emotion_scores["wariness"],
                    emotion_scores["anger"]
                ])
            print("[bold green]감정기록_날짜별.csv 파일로 저장했어![/bold green]")
            

            break
        elif user_input == "":
            recorded_emotions_list.append("회피")
            print("고민봇: 말 한마디 얼마나 어려울지 알아. 기다릴게 준비되면 편하게 말해줘.")
        else:
            for emo in detect_emotion(user_input):
                recorded_emotions_list.append(emo)
            print("고민봇:", respond(user_input))


TELEGRAM_TOKEN = "7745659258:AAHk0nFmVkbRKjDf2XgD6nesMIJYtlIEAn0"
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    bye_list = ["그만", "종료", "잘가", "bye", "ㅂㅂ"]

    if "recorded_emotions" not in context.chat_data:
        context.chat_data["recorded_emotions"] = []

    if user_input in bye_list:
        await update.message.reply_text("너와 함께 있어서 참 좋더라. 오늘 하루도 고생했어!!")
        stats = save_emotion(context.chat_data["recorded_emotions"])
        await update.message.reply_text(str(stats))
    elif user_input == "":
        context.chat_data["recorded_emotions"].append("회피")
        await update.message.reply_text("말 한마디 얼마나 어려울지 알아. 기다릴게 준비되면 편하게 말해줘.")
    else:
        emotions_detected = detect_emotion(user_input)
        context.chat_data["recorded_emotions"].extend(emotions_detected)
        await update.message.reply_text(respond(user_input))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("안녕! 지금 기분이 어떤지 말해줘.\n솔직하게 감정과 생각을 말해줘야 상담이 가능해 :)")


def telegram_main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("✅ 텔레그램 모드 실행 중... @theNoranbot 에서 사용 가능!")
    app.run_polling()

if __name__ == "__main__":
    mode = input("실행 모드 선택 (in = 콘솔 / out = 텔레그램): ").strip().lower()
    if mode == "in":
        main()
    elif mode == "out":
        telegram_main()
    else:
        print("❌ 잘못된 입력입니다. 'in' 또는 'out'을 입력해주세요.")