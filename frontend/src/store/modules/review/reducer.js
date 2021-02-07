import { SET_REVIEW, SET_REVIEWS } from './actions';

export const initialState = {
  detail: undefined,
  list: undefined,
}

const reviewReducer = function (state = initialState, action) {
  switch (action.type) {
    case SET_REVIEW:
      return {
        ...state,
        detail: action.payload.detail,
      }
    case SET_REVIEWS:
      return {
        ...state,
        list: action.payload.list,
      }
    default:
      return state;
  }
}

export default reviewReducer;
