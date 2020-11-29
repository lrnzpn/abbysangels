export const state = () => ({
    userLoc: null,
  })
  
export const mutations = {
    userLocation(state, location) {
        state.userLoc = location
    }
}