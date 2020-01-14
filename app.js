const express = require('express');
const app = express();

const path = require('path');
const fs = require('fs');

app.use(express.static('static'));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile('/index.html')
    fs.readFile('titles.json', { encoding: 'utf-8' }, (err, file) => {
        const data = JSON.parse(file);
        res.locals.data = data;
    })
});
app.post('/search', async (req, res) => {
    const title = (req.body.title).toString();
    console.log(title)
    let titles = res.locals.data;
    const result = []
    if (titles == undefined) {
        fs.readFile('titles.json', { encoding: 'utf-8' }, (err, file) => {
            if (err) throw err;
            const data = JSON.parse(file);
            titles = data;
            for (const t in titles) {
                
                if(titles[t].toLowerCase().includes(title)){
                    result.push(titles[t]);
                }
            }
            res.json(result);
        })
    }else{
        for (const t in titles) {
            if(titles[t].toLowerCase().includes(title)){
                result.push(titles[t]);
            }
        }
        res.json(result);
    }




});

app.post('/',async (req,res)=>{
    const title = (req.body.title).toString();
    

    let runPy = new Promise(function(success, nosuccess) {
        const spawn = require('child_process').spawn;
        const pythonProcess = spawn('python',["model.py",title]);
        pythonProcess.stdout.on('data', function(data) {
            
            success(data);
        });
    
        pythonProcess.stderr.on('data', (data) => {
    
            nosuccess(data);
        });
    });
    
    runPy.then((data)=>{
        result = JSON.parse(data.toString())
        res.json(result)
     
    }
    ).catch(err=>console.log(err));

   
    
});


app.listen(3000, console.log("Server started!"));
