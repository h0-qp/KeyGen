const { exec } = require("child_process");

// تشغيل ملف Python
exec("python bot.py", (error, stdout, stderr) => {
    if (error) {
        console.error(خطأ: ${error.message});
        return;
    }
    if (stderr) {
        console.error(خطأ: ${stderr});
        return;
    }
    console.log(ناتج: ${stdout});
});
