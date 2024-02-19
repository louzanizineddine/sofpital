<template>
    <Header />
    <div id="videos">
        <video id="learner" class="video-player" autoplay playsinline>
        </video>
        <video id="tutor" class="video-player" autoplay playsinline>
        </video>
    </div>
</template>
<!--
<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import Header from './Header.vue';
import AgoraRTC from 'agora-rtc-sdk-ng'

let APPID = ''
let uid = String(Math.floor(Math.random() * 1000000000))

let client;
let chanel;

const servers = {
    iceServers: [
        {
            urls: ['stun:stun1.1.google.com:19302', 'stun:stun2.1.google.com:19302']
        }
    ]
}

let localStream = ref(null)
let remoteStream = ref(null)
let peerConnection = ref(null)

let init = async () => {
    // client = AgoraRTC.createClient()
    // await client.login({ uid: uid, token: null })

    // chanel = client.createChannel('main')
    // await chanel.join()

    // chanel.on('MemberJoined', handleMemberJoined);

    localStream.value = await navigator.mediaDevices.getUserMedia({ video: true, audio: false})
    document.getElementById('learner').srcObject = localStream.value

    createOffer()
} 

init();

let createOffer = async () => {
    peerConnection.value = new RTCPeerConnection(servers)
    remoteStream.value = new MediaStream()
    document.getElementById('tutor').srcObject = remoteStream.value


    localStream.value.getTracks().forEach(track => {
        peerConnection.value.addTrack(track, localStream.value)
    });


    peerConnection.value.onTrack = (event) => {
        event.streams[0].getTracks().forEach(track => {
            remoteStream.value.addTrack(track);
        })
    }


    peerConnection.value.onicecandidate = async (event) => {
        if (event.candidate){
            console.log('new icecondidate' + event.candidate)
        }
    }


    let offer = await peerConnection.value.createOffer()
    await peerConnection.value.setLocalDescription(offer)

    console.log('offer:', offer)
}

let handleMemberJoined = async (memberId) => {
    console.log('member joined', memberId);

}

</script>

<style scoped>
#videos {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.video-player {
    width: 100%;
    height: 300px;
    border-radius: 10px;
    background-color: #000;
}

#learner {
    grid-column: 1 / 2;
    grid-row: 1 / 2;
}
</style> -->