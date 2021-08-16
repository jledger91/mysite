import { SET_CONFIG } from './actions';

export const initialState = {
  googleClientId: undefined,
}

const configReducer = function (state = initialState, action) {
  switch (action.type) {
    case SET_CONFIG:
      return {
        ...action.payload,
      }
    default:
      return state;
  }
}

export default configReducer;
