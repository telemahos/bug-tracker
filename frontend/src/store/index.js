import { createStore } from 'vuex'

export default createStore({
  state: {
    sidebarVisible: '',
    sidebarUnfoldable: false,
    isAuthenticated: false,
    token: '',
    isLoading: false,
    apiURL: 'http://127.0.0.1:8000/api',
    today: '',
  },
  mutations: {
    toggleSidebar(state) {
      state.sidebarVisible = !state.sidebarVisible
    },
    toggleUnfoldable(state) {
      state.sidebarUnfoldable = !state.sidebarUnfoldable
    },
    updateSidebarVisible(state, payload) {
      state.sidebarVisible = payload.value
    },
    initializeApp(state) {
      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
          state.today = new Date()
          console.log("initializeApp Token", state.token)
          console.log("initializeApp TODAY: ", state.today)
          console.log("initializeApp isAuthenticated", state.isAuthenticated)
      } else {
          state.token = ''
          state.isAuthenticated = false
          // console.log("initializeApp Token", state.token)
          console.log("initializeApp isAuthenticated", state.isAuthenticated)
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
      console.log("setIsLoading")
    },
    setToken(state, token) {
        state.token = token
      state.isAuthenticated = true
      // state.today = new Date()
      // console.log("initializeApp TODAY22: ", state.token)
        console.log("setToken")
    },
    removeToken(state) {
        localStorage.setItem('token','')
        state.token = ''
        state.isAuthenticated = false
        console.log("removeToken")
    },
  },
  actions: {},
  modules: {},
})
