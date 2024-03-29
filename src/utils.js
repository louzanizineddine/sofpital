// import { atob } from 'atob';

import {apiURL} from "./config"

function checkToken ()
{
    const token = localStorage.getItem('token');
    if (token == null) return null;
    const decoded = JSON.parse(atob(token.split('.')[1]));
    return decoded;
}


async function getTutorInfo(tutorId){
    const response = await fetch(`${apiURL}tutor/${tutorId}`,
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

async function getLearnerInfo(learnerId){
    const response = await fetch(`${apiURL}learner/${learnerId}`,
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
    const response = await fetch(`${apiURL}learner/${learnerId}/posts/${postId}`,
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
  let date = new Date(dateString);
  
  // Get day and month
  let day = date.getDate();
  let month = date.getMonth() + 1; // Months are zero-indexed
  let year = date.getFullYear();
  // Pad single digit day and month with leading zero
  day = day < 10 ? '0' + day : day;
  month = month < 10 ? '0' + month : month;
//   year = year < 10 ? '0' + year : year;
  
  // Return formatted date string in "dd/mm" format
  return day + '/' + month + '/' + year;
}



export { checkToken, getTutorInfo, getLearnerInfo ,getPostInfo, formatDate };
