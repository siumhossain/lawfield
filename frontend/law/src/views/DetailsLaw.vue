<template >
    <div>
        <div class="container">
            <div class="row my-5 mx-2">
                <i @click="back()" class="fas fa-long-arrow-alt-left"> Back</i>
                
            </div>
            <div class="row">
                <div class="col ">
                    <div v-for="i in obj" :key="i.id">
                        <div class="card mb-3">
                            <div class="card-body">
                                <h5 class="card-title">{{i.title}}</h5>
                                <p class="card-text">
                                    <span v-html="i.description"></span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        
            
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'DetailsLaw',
    data(){
        return {
            obj:[]
        }
    },
    methods:{
        back(){
            this.$router.go(-1)
        }
    },
    async created(){
        delete  axios.defaults.headers.common["Authorization"];
        const id = this.$route.params.id
        await axios.get(`api/lawDescription/${id}/`)
        .then(res => {
            console.log(res.data)
            this.obj = res.data
            axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
        })
        .then(err => {
            console.log(err)
            axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
        })
    }
}
</script>
<style >
    
</style>