import { createStore } from 'vuex'

export default createStore({
  state: {
    user:null,
    about:[]
    
  },
  
  actions: {
    user(context,user){
      context.commit('user',user)
    },
    about(context,about){
      context.commit('about',about)
    }
    

  },

  mutations: {
    user(state,user){
      state.user = user
    },
    about(state,about){
      state.about = about
    }
    
  },
  
  
})