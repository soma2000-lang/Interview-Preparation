using my.bookshop as my from '../db/data-model';
using { ECEmploymentInformation} from './external/ECEmploymentInformation';
using { ECTimeOff} from './external/ECTimeOff';

service CatalogService {
    @readonly entity EmpJob as projection on ECEmploymentInformation.EmpJob {userId};
    @readonly  entity EmployeeTime as projection on ECTimeOff.EmployeeTime { userId,startDate,endDate,approvalStatus,timeType};

}


   
    
       
    