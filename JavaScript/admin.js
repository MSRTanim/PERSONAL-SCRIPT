module.exports.config = {
	name: "inf",
	version: "1.0.1", 
	hasPermssion: 0,
	credits: "Joshua Sy", //don't change the credits please
	description: "Admin and Bot info.",
	commandCategory: "...",
	cooldowns: 1,
	dependencies: 
	{
    "request":"",
    "fs-extra":"",
    "axios":""
  }
};
module.exports.run = async function({ api,event,args,client,Users,Threads,__GLOBAL,Currencies }) {
const axios = global.nodemodule["axios"];
const request = global.nodemodule["request"];
const fs = global.nodemodule["fs-extra"];
const time = process.uptime(),
		hours = Math.floor(time / (60 * 60)),
		minutes = Math.floor((time % (60 * 60)) / 60),
		seconds = Math.floor(time % 60);
const moment = require("moment-timezone");
var juswa = moment.tz("Asia/Dhaka").format("『D/MM/YYYY』 【hh:mm:ss】");
var link = ["https://i.imgur.com/DCHau9c.jpg",
            "https://i.imgur.com/byPN9Xj.jpg",
            "https://i.imgur.com/gOmj7AT.jpg",
            "https://i.imgur.com/fMt67O7.jpg",
            
"https://i.imgur.com/H4qYXw5.jpg"];var callback = () => api.sendMessage({body:`🌺𝐁4𝐃9𝐋☘️𝐕41🍀𝐁𝐎𝐓-007🌺 

☘️𝐁𝐎𝐓 𝐍𝐀𝐌𝐄 : ${global.config.BOTNAME}🌺𝐁4𝐃9𝐋☘️

🌺𝐁𝐎𝐓 𝐀𝐃𝐌𝐈𝐍 : ☘️『𝐁𝐀𝐃𝐎𝐋✓𝐂𝐇𝐎𝐖𝐃𝐇𝐔𝐑𝐘』🌺

☘️𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 : https://www.facebook.com/itz.BADOL.Vai.420

🌺𝐁𝐎𝐓 𝐏𝐑𝐄𝐅𝐈𝐗 : ${global.config.PREFIX}

☘️𝐁𝐎𝐓 𝐎𝐖𝐍𝐄𝐑 : 🌺『বৃা্ঁদৃা্ঁলৃ্ঁ🍁চোৃ্ঁধুৃ্ঁরীৃ্ঁ 』☘️

🌺➟ 𝐔𝐏𝐓𝐈𝐌𝐄☘️

☘️𝐓𝐎𝐃𝐀𝐘 𝐈𝐒 𝐓𝐈𝐌𝐄 : ${juswa} 

🌺𝐁𝐎𝐓 𝐈𝐒 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 ${hours}:${minutes}:${seconds}.

𝐓𝐇𝐀𝐍𝐊𝐒 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 ${global.config.BOTNAME}🌺𝐁4𝐃9𝐋☘️


『༆𝐌𝐘🌺☘️ 𝐁𝐎𝐒𝐒👉(𝐁 𝐀 𝐃 𝐎 𝐋 𝐕 𝐀 𝐈 )✪\n\n𝐂𝐑𝐀𝐃𝐈𝐓✯𝘽𝙔:𝐁4𝐃9𝐋᯽𝐕41★𝐁 𝐎 𝐓✰0 0 7🌺☘️༆』`,attachment: fs.createReadStream(__dirname + "/cache/juswa.jpg")}, event.threadID, () => fs.unlinkSync(__dirname + "/cache/juswa.jpg")); 
      return request(encodeURI(link[Math.floor(Math.random() * link.length)])).pipe(fs.createWriteStream(__dirname+"/cache/juswa.jpg")).on("close",() => callback());
   };