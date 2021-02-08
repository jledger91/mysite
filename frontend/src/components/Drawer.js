import { useHistory } from 'react-router';

import {
  Divider,
  Drawer as MuiDrawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
} from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';
import MovieIcon from '@material-ui/icons/Movie';
import PersonIcon from '@material-ui/icons/Person';
import RateReviewIcon from '@material-ui/icons/RateReview';

import {
  FILM_LIST,
  REVIEW_LIST,
  USER_LIST,
} from '../routes';

import './Drawer.scss';

const Drawer = (props) => {
  
  const { onClose, open } = props;
  
  const history = useHistory();
  
  const items = [
    {
      label: 'Films',
      icon: <MovieIcon/>,
      path: FILM_LIST,
    },
    {
      label: 'Reviews',
      icon: <RateReviewIcon/>,
      path: REVIEW_LIST,
    },
    {
      label: 'Users',
      icon: <PersonIcon/>,
      path: USER_LIST,
    },
  ];
  
  const handleOnClick = (path) => () => {
    onClose();
    history.push(path);
  }
  
  return (
    <MuiDrawer className='drawer'
               open={open}
               onClose={onClose}>
      <List className='list'>
        <ListItem className='list-item'
                  button
                  onClick={onClose}>
          <ListItemIcon><MenuIcon/></ListItemIcon>
        </ListItem>
        <Divider/>
        {
          items.map(item =>
            <ListItem className='list-item'
                      button
                      key={item.label}
                      onClick={handleOnClick(item.path)}>
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText>{item.label}</ListItemText>
            </ListItem>
          )
        }
      </List>
    </MuiDrawer>
  );
}

export default Drawer;
