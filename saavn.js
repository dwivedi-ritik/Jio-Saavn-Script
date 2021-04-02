const axios = require("axios")
    
let arg_arr = process.argv.slice(2)
let type = arg_arr[1]
let link = arg_arr[0]

function decrypt(url){
	url = url.replaceAll("+" , "%2B")
	url = url.replaceAll("/" , "%2F")
	return url
}

function signUrl(encryptUrl , title){
    axios({
        method:"get",
        url:"https://www.jiosaavn.com/api.php?__call=song.generateAuthToken",
        params :{
            "url":decrypt(encryptUrl),
            "api_version" : "4" ,
            "_format" : "json",
            "_marker" : "0" , 
            "bitrate": "128"
        }
    })
    .then(res=>{
        let songUrl = res.data.auth_url
        let obj = {
            "title":title,
            "url": songUrl,
            "success":true,
        }
        console.log(obj)
    })
}
async function saavn(url , type){
    let resp = await axios({
        method:"get",
        url:"https://www.jiosaavn.com/api.php?__call=webapi.get",
        params :{
            "api_version" : "4" ,
            "_format" : "json",
            "_marker" : "0",
            "token" : url,
            "type":type
        }
    })
    let out = await resp.data
    return out
}

let out = saavn(link , type)

var twirlTimer = (function() {
    var P = ["\\", "|", "/", "-"];
    var x = 0;
    return setInterval(function() {
      process.stdout.write("\r" + "Waiting for URL " +P[x++]);
      x &= 3;
    }, 250);
  })();


out.then(res => {
    clearInterval(twirlTimer)
    if (type == "album"){
        for(let obj of res.list){
            signUrl(obj.more_info.encrypted_media_url , obj.title)
        }

    }else{
        let keyObj
        for(let key in res)keyObj = key
        signUrl(res[keyObj].more_info.encrypted_media_url , res[keyObj].title)
    }
})
