from win32com.client import Dispatch 
import requests
def spe(str):
    sp=Dispatch("SAPI.SpVoice")
    sp.Speak(str)

if __name__=='__main__':
    spe("Hello. I am your news reader. Presenting today's Top 10 news ")
    res = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=7d6fe3e9980849b6b60801f62abd5418").json()
    results=res['articles'] # this is dictionary res['title],res[description],res['content]
    i=1
    for news in results:
        print(news['title'])
        spe(news['title'])
        if(news['description']!=None):
            print(news['description'])
            spe(news['description'])
        #spe(news['title']+". "+news['description'])
        i+=1
        if(i==10):
            break
    spe("This was your top 10 news for today. See you tomorrow.")
        


    
