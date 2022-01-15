<template >
    <div>
        <div class="conatiner mx-3 my-4">
          <h1>Dashboard</h1>
          <table class="table table-hover">
                <thead>
                <tr>
                <th scope="col">Client id</th>
                <th scope="col">Subject</th>
                <th scope="col"></th>
                
                </tr>
            </thead>
            <tbody>
                <tr v-for="i in obj" :key="i.id">
                <th scope="row">{{i.client}}</th>
                <td>{{i.message}}</td>
                <td> <button @click="details(i.id)" class="btn btn-primary">Details</button> </td>
                
                </tr>
            </tbody>
          </table>
       </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'LawyerDash',
    data(){
        return{
            id:this.$store.state.user.id,
            obj:[]
        }
    },
    methods:{
        details(id){
            console.log(id)
            this.$router.push(`/appointmentDetails/${id}`)
        }
    },
    async created(){
        await axios.get(`api/appointmentDetails/${this.id}/`)
        .then(res => {
            console.log(res.data)
            this.obj = res.data
        })
    }
}
</script>
<style >
    
</style>