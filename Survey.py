from selenium import webdriver
from random import randint
from time import sleep
from json import load, dumps

answers = []
stage2 = []
stage3 = []
stage4 = []
stage5 = []
stage6 = []
stage7 = []
stage8 = []
stage9 = []
onlyProbableAnswers = [5, 6, 8, 12]

def completeSurvey():
    # Perceived Access
    webkey.find_element_by_id("label-access_buy-" + answers[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-access_people-" + answers[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-access_store-" + answers[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-access_dispensary-" + answers[3]).click()
    sleep(2)
    webkey.find_element_by_id("label-access_card-" + str(randint(1, 3))).click()
    sleep(2)
    webkey.find_element_by_id("label-access_kids-" + answers[4]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Source
    webkey.find_element_by_id("id-__chk__source_30_days_2_RC_" + answers[5]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Lifetime Marijuana Use
    webkey.find_element_by_id("label-life_use_all-" + answers[6]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Monthly Marijuana Use
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Susceptibility
    webkey.find_element_by_id("label-susceptibility_1-" + stage2[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-susceptibility_2-" + stage2[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-susceptibility_3-" + stage2[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-susceptibility_4-" + stage2[3]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # How Marijuana Makes People Feel
    webkey.find_element_by_id("label-meeq_1-" + stage3[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-meeq_2-" + stage3[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-meeq_3-" + stage3[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-meeq_4-" + stage3[3]).click()
    sleep(2)
    webkey.find_element_by_id("label-meeq_5-" + stage3[4]).click()
    sleep(2)
    webkey.find_element_by_id("label-meeq_6-" + stage3[5]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Perceived Harm
    webkey.find_element_by_id("label-harm_month-" + stage4[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-harm_weekly-" + stage4[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-harm_regularly-" + stage4[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-harm_school-" + stage4[3]).click()
    sleep(2)
    webkey.find_element_by_id("label-harm_car-" + stage4[4]).click()
    sleep(2)
    webkey.find_element_by_id("label-harm_pass-" + stage4[5]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Perceived Social Norms
    webkey.find_element_by_id("label-norms_friends-" + stage5[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-norms_1-" + stage5[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-norms_2-" + stage5[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-norms_3-" + stage5[3]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Substance Use
    webkey.find_element_by_id("label-sub_cigs-" + stage6[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-sub_cigars_days-" + stage6[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-sub_chew_days-" + stage6[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-sub_vape-" + stage6[3]).click()
    sleep(2)
    webkey.find_element_by_id("label-sub_quit-" + stage6[4]).click()
    sleep(2)
    webkey.find_element_by_id("label-sub_alcohol_days-" + stage6[5]).click()
    sleep(2)
    webkey.find_element_by_id("label-sub_rx-" + stage6[6]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Advertising
    webkey.find_element_by_id("label-advertise_1-" + stage7[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-advertise_2-" + stage7[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-advertise_email-" + stage7[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-advertise_coupon-" + stage7[3]).click()
    sleep(2)
    webkey.find_element_by_id("label-advertise_billboard-" + stage7[4]).click()
    sleep(2)
    webkey.find_element_by_id("label-advertise_news-" + stage7[5]).click()
    sleep(2)
    webkey.find_element_by_id("label-advertise_truck-" + stage7[6]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Resilience
    webkey.find_element_by_id("label-res_1-" + stage8[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-res_2-" + stage8[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-res_3-" + stage8[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-res_4-" + stage8[3]).click()
    sleep(2)
    webkey.find_element_by_id("label-res_5-" + stage8[4]).click()
    sleep(2)
    webkey.find_element_by_id("label-res_6-" + stage8[5]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    # Culture
    webkey.find_element_by_id("label-culture_1-" + stage9[0]).click()
    sleep(2)
    webkey.find_element_by_id("label-culture_2-" + stage9[1]).click()
    sleep(2)
    webkey.find_element_by_id("label-culture_3-" + stage9[2]).click()
    sleep(2)
    webkey.find_element_by_id("label-culture_4-" + stage9[3]).click()
    sleep(2)
    webkey.find_element_by_name("submit-btn-saverecord").click()
    sleep(2)
    webkey.find_element_by_xpath("//div[@id='survey_queue']/div/div/div/div[2]/button/span").click()
    sleep(1)
    webkey.find_element_by_id("survey_queue_email_send").send_keys(emailaddy)
    sleep(1)
    webkey.find_element_by_css_selector(".jqbuttonmed:nth-child(2)").click()
    sleep(5)
    print("\n" + webkey.find_element_by_xpath("//div[11]/div[2]").text)
    webkey.close()
    print("\nSurvey is done!\nDetails are saved in details.json")

def ageCalculator(years):
    return 2007 - int(years)

def surveyPart():
    webkey.find_element_by_id("label-sex_birth-2").click()
    webkey.find_element_by_id("label-gender-" + str(randint(1, 7))).click()
    webkey.find_element_by_id("label-age-" + str(ageCalculator(yob))).click()
    webkey.find_element_by_id("label-grade-" + str(ageCalculator(yob))).click()
    webkey.find_element_by_id("id-__chk__race_RC_" + str(randint(1, 7))).click()
    sleep(1)
    webkey.find_element_by_name("submit-btn-saverecord").click()

    n = randint(1, 3)
    initializeAnswers(n)

    # 1 - no smoke
    # 2 - smoke some
    # 3 - yes i smoke a lot

def initializeAnswers(n):
    global answers
    global stage2
    global stage3
    global stage4
    global stage5

    # Stage 1
    while len(answers) < 5:
        answers.append(str(randint(n, n+1)))
    if n == 1:
        answers.append("1")
        answers.append("0")
    else:
        answers.append(str(onlyProbableAnswers[randint(0, 3)]))
        answers.append(str(randint(1, 4)))

    # Stage 2
    if n == 1:
        while len(stage2) < 4:
            stage2.append(str(randint(n+2, n+3)))
    elif n == 2:
        while len(stage2) < 4:
            stage2.append(str(randint(n, n+1)))
    elif n == 3:
        while len(stage2) < 4:
            stage2.append(str(randint(n-2, n-1)))

    # Stage 3
    while len(stage3) < 6:
        stage3.append(str(randint(2, 5)))

    # Stage 4
    if n == 1:
        stage4 = ["2", "3", "4", "0", "0", "0"]
    elif n == 2 or n == 3:
        stage4 = ["1", "2", "3"]
        while len(stage4) < 6:
            stage4.append(str(randint(0, 1)))

    # Stage 5
    stage5.append(str(randint(1, 5)))
    if n == 1:
        stage5.extend([str(randint(1, 3)), "1", "1"])
    elif n == 2 or n == 3:
        stage5.extend(["3", "2", str(randint(1, 3))])

    # Stage 6
    stage6.extend([str(randint(0, 1)), str(randint(1, 4)), str(randint(1, 4)), "0", "0", str(randint(1, 3)), str(randint(1, 5))])

    # Stage 7
    stage7.extend([str(randint(1, 7)), str(randint(1, 6)), str(randint(1, 4)), str(randint(1, 6)), str(randint(1, 4)), str(randint(1, 4)), str(randint(1, 4))])

    # Stage 8
    k = randint(1, 2)
    if k == 1:
        stage8.extend([str(randint(3, 5)), str(randint(1, 3)), str(randint(3, 5)), str(randint(1, 4)), str(randint(3, 5)), str(randint(1, 3))])
    elif k == 2:
        stage8.extend([str(randint(1, 3)), str(randint(3, 5)), str(randint(1, 3)), str(randint(2, 5)), str(randint(1, 3)), str(randint(3, 5))])

    # Stage 9
    stage9.extend([str(randint(1, 3)), str(randint(1, 3)), str(randint(1, 3)), str(randint(1, 2))])

    completeSurvey()

def globalDeclaration(key, dob, email):
    global emailaddy, webkey, yob
    emailaddy = email
    webkey = key
    yob = dob

    surveyPart()
