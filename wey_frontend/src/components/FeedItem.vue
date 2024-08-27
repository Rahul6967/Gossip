<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img :src="post.created_by.get_avatar" class="w-[40px] rounded-full">

            <p>
                <strong>
                    <RouterLink :to="{ name: 'profile', params: { 'id': post.created_by.id } }">{{ post.created_by.name }}
                    </RouterLink>
                </strong>
            </p>
        </div>

        <p class="text-gray-600">{{ post.created_by_formatted }} ago</p>
    </div>

    <template v-if="post.attachments.length">
        <img v-for="image in post.attachments" v-bind:key="image.id" :src="image.get_image" class="w-full mb-4 rounded-xl">
    </template>

    <p>{{ post.body }}</p>

    <div class="my-6 flex justify-between">
        <div class="flex space-x-6 items-center">
            <div class="flex items-center space-x-2" @click="likePost(post.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z">
                    </path>
                </svg>

                <span class="text-gray-500 text-xs">{{ post.likes_count }} likes</span>
            </div>

            <div class="flex items-center space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z">
                    </path>
                </svg>

                <RouterLink :to="{name: 'postview',params:{id: post.id}}" class="text-gray-500 text-xs">{{ post.comments_count }} comments</RouterLink>
            </div>

            <div v-if="post.is_private">

                <svg xmlns="http://www.w3.org/2000/svg" height="20" width="20" viewBox="0 0 448 512">
                    <path d="M144 144l0 48 160 0 0-48c0-44.2-35.8-80-80-80s-80 35.8-80 80zM80 192l0-48C80 64.5 144.5 0 224 0s144 64.5 144 144l0 48 16 0c35.3 0 64 28.7 64 64l0 192c0 35.3-28.7 64-64 64L64 512c-35.3 0-64-28.7-64-64L0 256c0-35.3 28.7-64 64-64l16 0z"/>
                </svg>
            
            </div>
            
        </div>

        <div>
            
            <div @click="toogleExtraModal">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z">
                    </path>
                </svg>
            </div>

        </div>
    </div>

    <div v-if="showExtraModal">
        <div class="flex space-x-6 items-center">
            <div class="items-center space-x-6 ps-3" @click="deletePost" v-if="userStore.user.id == post.created_by.id">
                <span class="text-red-500 text-sm">Delete</span>
            </div>
            <div class="items-center space-x-6 ps-3" @click="reportPost">
                <span class="text-yellow-500 text-sm">Report</span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import {useUserStore} from '@/stores/user'
import { useToastStore } from '@/stores/toast'

    export default {
        props: {
            post: Object
        },

        emits: ['deletePost'],

        setup() {
            const userStore = useUserStore()
            const toastStore = useToastStore()

            return {
                userStore,
                toastStore
            }
        },

        data() {
            return {
                showExtraModal: false
            }
        },

        methods: {
            likePost(id) {

                axios
                    .post(`/api/posts/${id}/like/`)
                    .then(response => {

                        if (response.data.message == 'like created') {
                            this.post.likes_count += 1
                        }
                    })
                    .catch(error =>{
                    console.log('error',error)
                    })
            },

            reportPost() {
                axios
                    .post(`/api/posts/${this.post.id}/report/`)
                    .then(response => {
                        console.log(response.data)

                        this.toastStore.showToast(5000, 'The post was reported','bg-yellow-500')
                    })
                    .catch(error =>{
                    console.log('error',error)
                    })
            },

            deletePost() {

                this.$emit('deletePost', this.post.id)

                axios
                    .delete(`/api/posts/${this.post.id}/delete/`)
                    .then(response => {
                        console.log(response.data)

                        this.toastStore.showToast(5000, 'The post was deleted','bg-red-500')
                    })
                    .catch(error =>{
                    console.log('error',error)
                    })
            },

            toogleExtraModal() {
                console.log('toogleExtraModal')

                this.showExtraModal = !this.showExtraModal
            }
        },

        components: {RouterLink}
    }
</script>