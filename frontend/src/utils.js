// import { atob } from 'atob';

function checkToken ()
{
    const token = localStorage.getItem('token');
    if (token == null) return null;
    const decoded = JSON.parse(atob(token.split('.')[1]));
    return decoded;
}


async function getTutorInfo(tutorId){
    const response = await fetch(`http://localhost:8000/api/tutor/${tutorId}`,
    {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token'),
        }
    });
    const data = await response.json();
    return data;
}

async function getPostInfo(learnerId,postId){
    const response = await fetch(`http://localhost:8000/api/learner/${learnerId}/posts/${postId}`,
    {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token'),
        }
    });
    const data = await response.json();
    return data;
}

function formatDate(dateString) {
  // Parse the date string
  var date = new Date(dateString);
  
  // Get day and month
  var day = date.getDate();
  var month = date.getMonth() + 1; // Months are zero-indexed
  
  // Pad single digit day and month with leading zero
  day = day < 10 ? '0' + day : day;
  month = month < 10 ? '0' + month : month;
  
  // Return formatted date string in "dd/mm" format
  return day + '/' + month;
}



export { checkToken, getTutorInfo, getPostInfo, formatDate };