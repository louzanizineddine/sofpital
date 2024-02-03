// import { atob } from 'atob';

export default function checkToken ()
{
    const token = localStorage.getItem('token');
    if (token == null) return null;
    const decoded = JSON.parse(atob(token.split('.')[1]));
    return decoded;
}
