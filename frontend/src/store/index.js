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
    all_projects: '',
    all_users: '',
    userRoles: [
      'No Role',
      'Admin',
      'Frontend Developer',
      'Backend Developer',
      'Full Stack Developer',
      'UI/UX Designer',
      'QA Analyst',
      'Business Analyst',
      'Product Manager',
      'Technology Manager',
    ],
    case_type: ['Issue', 'Bug', 'Note'],
    status: ['New', 'In Progress', 'On Hold', 'Solved'],
    priority: ['Normal', 'Medium', 'High', 'Critical'],
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
        console.log('initializeApp Token', state.token)
        console.log('initializeApp TODAY: ', state.today)
        console.log('initializeApp isAuthenticated', state.isAuthenticated)
      } else {
        state.token = ''
        state.isAuthenticated = false
        // console.log("initializeApp Token", state.token)
        console.log('initializeApp isAuthenticated', state.isAuthenticated)
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
      console.log('setIsLoading')
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
      // state.today = new Date()
      // console.log("initializeApp TODAY22: ", state.token)
      console.log('setToken')
    },
    removeToken(state) {
      localStorage.setItem('token', '')
      state.token = ''
      state.isAuthenticated = false
      console.log('removeToken')
    },
    // setProjects(state, projects) {
    //   state.all_projects = JSON.stringify(projects)
    //   console.log('STORE: all_projects' + state.all_projects)
    // },
    // setUsers(state, users) {
    //   state.all_users = JSON.stringify(users)
    //   console.log('STORE: all_users' + state.all_users)
    // },
  },
  actions: {},
  modules: {},
})
