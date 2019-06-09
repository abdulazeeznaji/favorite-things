import {
  FETCH_START,
  FETCH_END,
} from "./mutations.type";
import {FETCH_FAVORITES} from "./actions.type";

const state = {
  favorites: [],
  isLoading: true,
};

const getters = {
  favorites(state) {
    return state.favorites;
  },
  isLoading(state) {
    return state.isLoading;
  }
};

const actions = {
  [FETCH_FAVORITES]({ commit }, params) {
  }
};

const mutations = {
  [FETCH_START](state) {
    state.isLoading = true;
  },
  [FETCH_END](state, { favorites }) {
    state.favorites = favorites;
    state.isLoading = false;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
