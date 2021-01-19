using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class setTrigger : MonoBehaviour {
    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("OnTriggerEnter");
    }

    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
