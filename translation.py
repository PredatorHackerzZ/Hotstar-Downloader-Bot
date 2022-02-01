class Translation(object):

    START_TEXT = """Hi I am URL Uploader Robot
I Can Upload File/Video From Direct Link
I Can Download From YouTube,Googledrive,Hotstar etc.....

"""

    HELP_USER = """There Below Instructions Follow
    
1. Send Me A Tumbnail if required. It'll be saved permanently.💯
2. If Thumbnail Wasn't Set By You, It'll Be Auto Generated From The File.🥳
3. Send Me Any Link To Be Uploaded To Telegram.
4. Press /deletethumbnail To Delete Your Current Custom Thumbnail
5. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
NB : It is Recommended To Use A Custom Thumbnail Because, Some Time Won't Upload The File Without a Custom Thumbnail.
If Any Issue r help Contact @HB4All_Support
"""


    ABOUT_TEXT = """<b>🤖 My Name : @URL_Uploader_Robot</b>

<b>📝 Language : Python3</b>

<b>🌐 HB4All : <a href='https://t.me/hb4all'> HB4All </a></b>

<b>📔 Library : Pyrogram 1.0.7</b>

<b>🤖 HB4All Bot : 👉 <a href='https://t.me/hb4all_bot'>HB4All Bot</a></b>

<b>💎 Botlist : <a href='https://t.me/BotlistHB4All'> Bot List </a></b>"""



    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>⬇️</a>
🎞  - Stream format
📁  - File format
<i>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</i> 😇
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = """HB4All Robots V.2 

@HB4All_Bot - Chief Bot
@HB4All2_Bot -  Create Buttons In Post
@HB4AllSeries_Bot - Series Bot
@Renamer_Ro_Bot - You Can Rename Any File
@Tgfilestorerobot - Store File And Send Private Link
@URL_Uploader_Robot- Send Any Direct Link To Upload As Telegram File And Video
@Url_Uploaderv1_Robot - URl Uploader V.1
@Groups_Control_Bot - Control Your Group With Awesome Features
@FiltersRobot - Filter Bot For Groups
@Autofiltersrobot- Auto Filter And Manual Filters For Group
@File2VideoRobot - Bot Converts File2Video Or Video2File
@YTHB4AllBot - Download Youtube Videos
@FileStreamingRobot - Send File And Get Stream & Download Link
@FastLinkRobot- Generate TG File 2 Shareable Link Fast🤯
@Upload2telegraphbot - Get Permanent Link For Photos
@GDriveUploader_Robot - Upload To Your Drive
@GPLinkHBbot - Shorten Link To Gplink
@BitlyLinkHBbot - Shorten Link To Bitly Link (Ad-free)
@MegaDownloadHB4AllBot - Download Mega.nz Files
@MegaUploadHB4AllBot - Upload Fiels To Mega.nz Your Account 
@DoodstreamRobot - Upload 2 Your DoodStream Account
@CloudStreamRobot - Tg File To Stream Online And Download 
@MergeRobot - Merge 10Video In One Video 
@QRcode_HBbot - QR Code Decode & Encode
@SelenaGomez_Robot Movie Series Bot Works In Group
@MultiHBbot - Multi Purpose Robot
@HB4AllRobot - Multi Purpose Robot

Check The Bot Status - https://t.me/hb4all/169"""
    
    DOWNLOAD_START = "Trying to download to my Server, Wait For Some Time 😇\n\n@hb4all_support"
    
    UPLOAD_START = "Trying to upload.....📤"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nI cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved✅. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully.❎"

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "This seems to be a very slow URL.Get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    
