U
    �<c_�  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� dZdZdZdd� Ze�  e�d� zd dl	m	Z	 W n< e
k
r�   e�d	� ed
� e�d� d dl	m	Z	 Y nX zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX zd dlZW nF e
k
�r�   ed� e�d� ed
� e�d� d dlZeZY nX dd� Zdd� Zedk�r�e�  dS )�    N�cleara�                                           
[1;34;40m                  \             /            
[1;34;40m                   \___________/    won data 
[1;33;40m                   /           \             
[1;33;40m                  /   @     @   \            
[1;32;40m                 ||             ||          
[1;34;40m                  \   \_ __ _/  /            
[1;30;40m                   \___________/                        
a�    
[1;34;40m                  \             /            
[1;34;40m                   \___________/    not data 
[1;33;40m                   /           \             
[1;33;40m                  /   @     @   \            
[1;32;40m                 ||    _ _ _    ||           
[1;32;40m                  \   /     \   /            
[1;30;40m                   \___________/             
  zG[1;36;40m
___________________________________________________________
c                  C   s�   t �d� ttd��} | dks6| dks6| dks6| dkr@td� nVt �d� ttd��}|d	ksf|d
krnt�  n(|dks~|dkr�t �d� t�  nt�  d S )Nr   z[1;36;40mEnter password :- Z	jahoo9808Z	jahoo1998Zjahoo98Zjahoo20ZsuccesszL
[1;31;40mWrong password

[1;33;40mAre you want Reenter password(y/n) : - �y�Y�n�N)�os�system�str�input�print�login�exit)Zaa�b� r   �	jahoo4.pyr   #   s    
 


r   )�tqdmzpip3 install tqdmz%s Requests installed.zfile_auth.txt�rz![1;0;40mPaste Your Auth here :- �wzfile_url.txtzPaste Your URL here :- zwaiting.......zpip3 install requestsc            	      C   sj  t �d� dtdd�} t}ttd��}t �d� d}d}td� tt||�dd	d
�D �]}td� |dkr�td� ttd�dd�D ]}|d d }t	�
d� q�n�tj|| d�}t|�}|dkr�tt� n2|dkr�|d7 }tt� ntt� td� tt� |d7 }tdt|d �� tdt|�� td� ttd��D ]}|d d }t	�
d� �q6t �d� qTt�  d S )Nr   zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionz[1;36;40mEnter Amount - r   zprogramme completez >zprocess....)�asciiZdescz



zE[1;30;40mWaiting one and harf minutes opening Algorithm


[1;34;40m�   z #)r   �d   g      �?)Zheadersz<Response [204]>z<Response [200]>�   zC
[1;31;40m [retry] Check Again your internet connection... [retry]z"


[1;32;40m
Number of request : z[1;32;40m
NUMBER of Message : z.[1;33;40m
Wait For Next request
[1;32;40m


)r   r   �	file_auth�	file_url1�intr
   r   r   �range�time�sleep�requests�getr	   �no_data�won_data�line�again)	�headZurl�s�mZrr�jZrrrZrjZrequestr   r   r   �maini   sJ    
 �


r(   c                  C   sJ   t d�} | dks| dkr t�  n&| dks0| dkr8t�  ntd� | �  d S )Nz*[1;0;40m
Do Restart Algorithm :  (y/n) - r   r   r   r   z[1;30;40mReEnter)r
   r(   �quitr   )r#   r   r   r   r#   �   s    r#   �__main__)r   Zurllib�sysr   r   r!   r    r"   r   r   �ImportErrorr   �open�f�readr   �closer	   r
   �wr�writer   r   Zauthr(   r#   �__name__r   r   r   r   �<module>   sl   
















5
