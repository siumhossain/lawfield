<template >
    <div>
       <div class="conatiner">
          <div class="row my-5 mx-2">
                <i @click="back()" class="fas fa-long-arrow-alt-left"> Back</i>
                
         </div>
       </div>
       <div class=".container mx-2 my-3">
          <div class="card">
            <div class="card-body">
               <h5>Client id:{{obj.client}}</h5>
               <p class="card-text">
                  {{obj.message}}
               </p>
               <button type="button" class="btn btn-primary">Accept</button>
               <button type="button" class="btn btn-primary mx-2">Decline</button>
               <button @click="feedbackbox()" type="button" class="btn btn-primary">Feedback</button>
            </div>
         </div>
         <div v-if="feedback" class='my-3 mx-2'>
            <label for="exampleFormControlTextarea1">Please give your feedback</label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            <button type="button" class="btn btn-primary my-3">Submit</button>
         </div>
       </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
   name:'AppointmentDetails',
   data(){
      return{
         obj:[],
         feedback:false
      }
      
   },
   async created(){
      const id = this.$route.params.id
      axios.get(`api/appointmentInDetails/${id}/`)
      .then(res => {
         console.log(res.data)
         this.obj = res.data
      })
   },
   methods:{
      back(){
            this.$router.go(-1)
        },
        feedbackbox(){
           this.feedback = !this.feedback
        }
   }
}
</script>
<style >
    
</style>