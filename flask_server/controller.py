
def getResults(args) :

    print("---------------------")
    print(args)
    print("---------------------")

    # 1. 모종의 동작을 거쳐서 response를 위한 데이터 생성
    responses = {}
    responses["numOfRows"] = "abcabc"
    responses["pageNo"] = "1"
    responses["totalCount"] = "1"
    responses["resultCode"] = "00"
    responses["resultMsg"] = "NORMAL SERVICE"

    return responses
