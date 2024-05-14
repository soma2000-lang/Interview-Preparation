const cds = require('@sap/cds');
const {Timemanagement} =require("../handler");

(async function ()
    {
    sfecei = await cds.connect.to("ECEmploymentInformation");
    sfecei = await cds.connect.to("ECTimeOff");
    }
)();


class ECEmploymentInformation extends cds.ApplicationService
{
init()
{ 
    const {EmpJob}= cds.entities;

    this.on(["READ"] ,"EmpJob",async()=>{
        
        return await sfecei.send({
            query: SELECT.from("EmpJob").limit(5)
        });
    })


    
    return super.init();
}


}
module.exports ={ECEmploymentInformation,ECTimeOff};


