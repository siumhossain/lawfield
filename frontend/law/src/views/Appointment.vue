<template >
    <div>
        <div class="container my-5 ">
            <div v-if='uploaded === false' class="card  shadow-5">
            <div  class="card-header text-center"><h3>Take Appointment</h3> </div>
            <div class="card-body">
                <div v-if="errors">
                    <p class='error' v-for="error in errors" :key="error.id">
                        {{error.file}}
                    </p>
                </div>
                <h5 class="card-title">Describe your problem</h5>
                <form>
                    <div class="form-group">
                    
                    <textarea v-model="message" class="form-control" id="exampleFormControlTextarea1" rows="4"></textarea>
                    </div>
                    <h5 class="card-title mt-3">Upload your essential documents</h5>
                    <div class="input-group mb-3">
                        <input type="file" v-on:change="handleFile( $event )" class="form-control" id="inputGroupFile02" />
                        
                    </div>
                    <p class="info">
                        <em>* For uploading multiple file please make it as .zip file.</em>
                        <br>
                        <em>* Make sure your file name has no space. [ Ex: file_up.pdf 👍🏻 , file up.pdf ❌ ]</em>
                    </p>
                </form>
                
                
                
                <button v-if='upload === false' @click="submit()" class="btn btn-primary">Submit</button>
                <button v-if='upload' class="btn btn-primary" type="button" disabled>
                    <span
                        class="spinner-border spinner-border-sm"
                        role="status"
                        aria-hidden="true"
                    ></span>
                    <span class="visually-hidden">Loading...</span>
                </button>
            </div>
            
        </div>

        <div v-if='uploaded === true' class="card text-center">
            <div class="card-body">
                <h3 class="card-title">
                    Thank You !!!
                </h3>
                <p class="card-body">
                    keep your eye on <span>
                        <router-link to='/appointmentDetails'>appointment</router-link>
                        </span> section to check whether your lawyer accept your appointment or reject.
                    Or you can go back to <span>
                        <router-link to='/'>Homepage</router-link>
                    </span>
                </p>
            </div>
        </div>

        </div>
        
    </div>
    <router-view></router-view>
</template>
<script>
import axios from 'axios'
export default {
    name:"Appointment",

    data(){
        return{
            fromUser: this.$store.state.user.id,
            toUser:'',
            file:null,
            message:'',
            upload:false,
            uploaded:false,
            errors:[]


        }
    },
    created(){
        
        this.toUser = this.$route.params.id
    },
    methods:{
        handleFile(event){
            this.file = event.target.files[0]
        },
        async submit(){
            this.upload = true
            let _this = this
            const formData = new FormData();
            formData.append('file',this.file,this.file.name)
            formData.append('message',this.message)
            formData.append('fromUser',this.fromUser)
            formData.append('toUser',this.toUser)

            await axios.post('api/sendAppointment/',formData)
            .then(res => {
                console.log(res.data)
                this.upload = false
                this.uploaded = true
            })
            .catch(function (error) {
                if (error.response) {
                // Request made and server responded
                
                //console.log(error.response.data);
                _this.errors = error.response
                console.log(_this.errors)
                _this.upload = false
                
                
                
                
                } 

            });

        }
    }
}
</script>
<style >
.info{
    color: crimson;
}
.error{
    color: crimson;
}
</style>