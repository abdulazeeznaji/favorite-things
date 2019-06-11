import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import { API_URL } from "@/common/config";

const ApiService = {
  init() {
    Vue.use(VueAxios, axios);
    Vue.axios.defaults.baseURL = API_URL;
  },


  query(resource, params) {
    return Vue.axios.get(resource, params).catch(error => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
  get(resource, slug = "") {
    return Vue.axios.get(`${resource}/${slug}`).catch(error => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
};


export default ApiService;

export const FavoriteService = {
  query(type, params) {
    return ApiService.query("favorites" + (type === "feed" ? "/feed" : ""), {
      params: params
    });
  },
  get(slug) {
    return ApiService.get("favorites", slug);
  },
};
